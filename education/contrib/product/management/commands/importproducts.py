import urllib, urllib2, json
from pymongo import MongoClient
from datetime import datetime, timedelta
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.core.files.base import ContentFile
from education.core.utils import *
from education.contrib.file.models import Image
from education.contrib.product.models import *

class Command(BaseCommand):
    args = '<media_type> <count> <offset>'
    help = 'Import product data.'

    def handle(self, *args, **options):
        GLog('Importing product data.', 'header')

        # Set parameters.
        media_type = args[0]

        count =  99999999
        if len(args) >= 2:
            count = int(args[1])

        skip = 0
        if len(args) == 3:
            skip = int(args[2])
        i = skip + 1

        # Setup MongoDB connection.
        client = MongoClient(settings.EDUCATION_MONGODB_HOST, settings.EDUCATION_MONGODB_PORT)
        db = client[settings.EDUCATION_MONGODB_DATABASE]

        # Get and index review data.
        collection = db['node']
        products = collection.find({'type': 'csm_%s' % media_type})

        for product in products:
            print product.title

        """
        product_list = urllib2.urlopen('%s?mac=%s' % (settings.EDUCATION_REVIEW_DATA_LIST_URL % media_type, settings.EDUCATION_MIGRATION_MAC_ID))
        nid_list = json.loads(product_list.read())

        del nid_list[count:]
        del nid_list[0:skip]

        for nid in nid_list:
            product_item = urllib2.urlopen('%s/%s?mac=%s' % (settings.EDUCATION_REVIEW_DATA_ITEM_URL % media_type, nid, settings.EDUCATION_MIGRATION_MAC_ID))
            product_data = json.loads(product_item.read())

            try:
                product = Product.objects.get(nid=int(product_data['nid']))
            except Product.DoesNotExist:
                product = Product()

            created = datetime.fromtimestamp(int(product_data['created']))
            changed = datetime.fromtimestamp(int(product_data['changed']))

            action = 'SKIPPED'
            if product.changed is None:
                action = 'CREATED'
            elif product.changed.replace(tzinfo=None) < changed:
                action = 'UPDATED'

            if product.changed is None or product.changed.replace(tzinfo=None) < changed:
                # Save the image file.
                image = Image()
                image_url = '%s/%s' % (CSM_MIGRATION_BASE_URL, product_data['field_product_image'][0]['filepath'])
                if urllib.urlopen(image_url).getcode() != 404:
                    image_data = urllib2.urlopen(image_url, timeout=5)
                    file_content = ContentFile(image_data.read())
                    image.file.save(product_data['field_product_image'][0]['origname'], file_content)
                    image.save()

                # Save the product data.
                product = Product()
                product.nid = product_data['nid']
                product.title = product_data['title'].encode('utf8')
                product.type = product_data['type'].replace('csm_', '')
                product.image = image
                product.status = int(product_data['status'])
                product.created = created
                product.changed = changed
                product.save()

                # Save the extended product data.
                import_data = getattr(self, 'import_%s_data' % media_type)
                import_data(product, product_data)

            GLog('[%s] %s. %s - %s %s' % (action, i, product.type, product.nid, product_data['title']))
            i += 1
            """

    def import_app_data(self, product, product_data):
        """
        Imports the meta data specific for apps.
        """
        app = App()
        app.product = product
        app.price = product_data['field_app_price'][0]['value']
        app.requirements = product_data['field_app_requirements'][0]['value']
        app.size = product_data['field_app_size'][0]['value']
        app.subscription = product_data['field_app_subscription'][0]['value']
        app.version = product_data['field_app_version'][0]['value']
        app.save()

    def import_website_data(self, product, product_data):
        """
        Imports the meta data specific for websites.
        """
        website = Website()
        website.product = product
        website.url = product_data['field_website_url'][0]['url']
        website.save()

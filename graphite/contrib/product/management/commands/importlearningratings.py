import urllib, urllib2, json
from pymongo import MongoClient
from datetime import datetime, timedelta
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.core.files.base import ContentFile
from graphite.core.utils import *
from graphite.contrib.file.models import Image
from graphite.contrib.product.models import *

class Command(BaseCommand):
    args = '<count> <offset>'
    help = 'Import Learning Ratings data.'

    def handle(self, *args, **options):
        GLog('Importing Learning Ratings data.', 'header')

        # Set parameters.
        count =  99999999
        if len(args) >= 2:
            count = int(args[1])

        skip = 0
        if len(args) == 3:
            skip = int(args[2])
        i = skip + 1

        # Setup MongoDB connection.
        client = MongoClient(settings.GRAPHITE_MONGODB_HOST, settings.GRAPHITE_MONGODB_PORT)
        db = client[settings.GRAPHITE_MONGODB_DATABASE]

        # Get and index review data.
        collection = db['node']
        reviews = collection.find({'type': 'csm_learning_rating'})

        for data in reviews:
            try:
                review = EditorialReview.objects.get(nid=int(data['nid']))
            except EditorialReview.DoesNotExist:
                review = EditorialReview()

            created = datetime.fromtimestamp(int(data['created']))
            changed = datetime.fromtimestamp(int(data['changed']))

            action = 'SKIPPED'
            if review.changed is None:
                action = 'CREATED'
            elif review.changed.replace(tzinfo=None) < changed:
                action = 'UPDATED'

            if review.changed is None or review.changed.replace(tzinfo=None) < changed:
                # Save the review data.
                review = EditorialReview()
                review.nid = data['nid']
                review.title = data['title'].encode('utf8')
                review.type = data['type'].replace('csm_', '')
                review.status = int(data['status'])
                review.created = created
                review.changed = changed
                review.save()

                # Save the extended product data.
                # import_data = getattr(self, 'import_%s_data' % media_type)
                # import_data(review, data)

            GLog('[%s] %s. %s - %s %s' % (action, i, review.type, review.nid, data['title']))
            i += 1

        """
        product_list = urllib2.urlopen('%s?mac=%s' % (settings.GRAPHITE_REVIEW_DATA_LIST_URL % media_type, settings.GRAPHITE_MIGRATION_MAC_ID))
        nid_list = json.loads(product_list.read())

        del nid_list[count:]
        del nid_list[0:skip]

        for nid in nid_list:
            product_item = urllib2.urlopen('%s/%s?mac=%s' % (settings.GRAPHITE_REVIEW_DATA_ITEM_URL % media_type, nid, settings.GRAPHITE_MIGRATION_MAC_ID))
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

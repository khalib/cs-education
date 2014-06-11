import urllib, urllib2, json
from pymongo import MongoClient
from datetime import datetime, timedelta
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.core.files.base import ContentFile
from education.core.utils import *
from education.contrib.file.models import Image
from education.contrib.user.models import *

class Command(BaseCommand):
    args = '<count> <offset>'
    help = 'Import user data.'

    def handle(self, *args, **options):
        GLog('Importing user data.', 'header')

        # Set parameters.
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
        collection = db['users']
        users = collection.find({})

        for data in users:
            try:
                user = User.objects.get(uid=int(data['uid']))
            except User.DoesNotExist:
                user = User()

            created = datetime.fromtimestamp(int(data['created']))
            login = datetime.fromtimestamp(int(data['login']))

            action = 'SKIPPED'
            if user.login is None:
                action = 'CREATED'
            elif user.login.replace(tzinfo=None) < login:
                action = 'UPDATED'

            if user.login is None or user.login.replace(tzinfo=None) < login:
                # Save the user data.
                user = User()
                user.uid = data['uid']
                user.email = data['mail'].encode('utf8')
                user.username = data['name'].encode('utf8')
                user.status = int(data['status'])
                user.created = created
                user.login = login
                user.save()

            GLog('[%s] %s. %s - %s %s' % (action, i, user.uid, user.username, data['mail']))
            i += 1
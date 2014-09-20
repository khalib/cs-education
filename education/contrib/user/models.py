from django.db import models
# from education.core.models import BaseModel


class User(object):
    def __init__(self, data=None):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']

"""
class User(BaseModel):
    uid = models.IntegerField(null=False)
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    status = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    login = models.DateTimeField(auto_now_add=True)
"""
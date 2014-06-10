from django.db import models
from graphite.core.models import BaseModel

class User(BaseModel):
    uid = models.IntegerField(null=False)
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    status = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    login = models.DateTimeField(auto_now_add=True)
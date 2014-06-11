from django.db import models
from education.core.models import BaseModel


class File(BaseModel):
    class Meta:
        abstract = True

    name = models.CharField(max_length=255, null=False)
    mime_type = models.CharField(max_length=32, null=False)

class Image(File):
    file = models.ImageField(upload_to='files/images', null=False, width_field='width', height_field='height', max_length=255)
    width = models.IntegerField()
    height = models.IntegerField()

    def __unicode__(self):
        return self.file
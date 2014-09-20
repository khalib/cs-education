from django.db import models
from education.core.models import BaseModel, ContentModel, NodeContentModel
from education.core.models import NodeObject

class Product(NodeObject):
    pass

class App(Product):
    pass

class Game(Product):
    pass

class Website(Product):
    pass

class Movie(Product):
    pass

"""
class Product(ContentModel):
    nid = models.IntegerField()
    type = models.CharField(max_length=32)
    # image = models.OneToOneField(Image, null=True)

    def __unicode__(self):
        return self.title

class App(BaseModel):
    product = models.OneToOneField(Product)
    price = models.CharField(max_length=64, null=True)
    requirements = models.CharField(max_length=255, null=True)
    size = models.CharField(max_length=32, null=True)
    subscription = models.CharField(max_length=255, null=True)
    version = models.CharField(max_length=64, null=True)

class Website(BaseModel):
    product = models.OneToOneField(Product)
    url = models.URLField(max_length=255)

class Game(BaseModel):
    product = models.OneToOneField(Product)

class EditorialReview(NodeContentModel):
    # product = models.OneToOneField(Product)
    a = 123

class UserReview(ContentModel):
    product = models.OneToOneField(Product)

DROP TABLE product_editorialreview, product_userreview, product_app, product_game, product_product, product_website;

class Book(BaseModel):
    product = models.OneToOneField(Product)
    hardcover_price = models.DecimalField(null=True)
    paperback_price = models.DecimalField(null=True)
    isbn = models.CharField(max_length=32, null=True)
    pages = models.IntegerField(null=True)
    recommended_reading_age_min = models.IntegerField(null=True)
    recommended_reading_age_max = models.IntegerField(null=True)
    read_alone_age_min = models.IntegerField(null=True)
    read_alone_age_max = models.IntegerField(null=True)
    read_aloud_age_min = models.IntegerField(null=True)
    read_aloud_age_max = models.IntegerField(null=True)
    release_date = models.DateTimeFied(null=True)

class Movie(BaseModel):
    product = models.OneToOneField(Product)
    mpaa_description = models.CharField(max_length=255, null=True)
    runtime = models.IntegerField(null=True)
    bestbuy_id = models.CharField(max_length=64, null=True)
    netflix_id = models.CharField(max_length=64, null=True)
    theatre_release_date = models.DateTimeFied(null=True)
    dvd_release_date = models.DateTimeFied(null=True)

class Music(BaseModel):
    product = models.OneToOneField(Product)
"""
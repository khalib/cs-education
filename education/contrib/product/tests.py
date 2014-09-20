import json
from django.test import TestCase
from education.contrib.product.models import Product

NODE_DATA = {
    'id': 123,
    'author': {
        'id': 111,
        'first_name': 'Foo',
        'last_name': 'Bar',
    },
    'status': 1,
    'title': 'FooBar',
    'type': 'app',
    'created': '2013-12-12T14:40:02.000Z',
    'changed': '2014-12-12T14:40:02.000Z',
    'url': 'http://www.foo.com/bar-app',
}

class ProductTest(TestCase):
    def test_product_init(self):
        product = Product(NODE_DATA)
        self.assertEquals(product.id, 123)
        self.assertEquals(product.type, 'app')
        self.assertEquals(product.status, 1)
        self.assertEquals(product.title, 'FooBar')
        self.assertEquals(product.created, '2013-12-12T14:40:02.000Z')
        self.assertEquals(product.changed, '2014-12-12T14:40:02.000Z')
        self.assertEquals(product.author.id, 111)
        self.assertEquals(product.author.first_name, 'Foo')
        self.assertEquals(product.author.last_name, 'Bar')


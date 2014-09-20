from django.test import TestCase

from education.libraries.cse.models.node import Node
from education.libraries.cse.models.product import Product, App

NODE_DATA = {
    'id': 123,
    'title': 'This is the title',
    'type': 'foo',
    'status': 1,
    'created': 1234567890,
    'changed': 1234567890,
}

PRODUCT_DATA = {
    'image': 'http://latimesphoto.files.wordpress.com/2010/11/giants_parade07.jpg'
}

class CSEModelNodeTest(TestCase):
    def test_node(self):
        node = Node(NODE_DATA)
        self.assertEquals(node.id, 123)
        self.assertEquals(node.title, 'This is the title')
        self.assertEquals(node.type, 'foo')
        self.assertEquals(node.status, 1)
        # self.assertEquals(node.created, 'foo')
        # self.assertEquals(node.changed, 'foo')

class CSEModelProductTest(TestCase):
    def test_product(self):
        product = Product(dict(NODE_DATA.items() + PRODUCT_DATA.items()))
        self.assertEquals(product.id, 123)
        self.assertEquals(product.title, 'This is the title')
        self.assertEquals(product.type, 'foo')
        self.assertEquals(product.status, 1)

    def test_get_url(self):
        product = Product(dict(NODE_DATA.items() + PRODUCT_DATA.items()))
        self.assertEquals(product.get_url(), '/products/123')

class CSEModelProductAppTest(TestCase):
    def test_product_app(self):
        app = App(dict(NODE_DATA.items() + PRODUCT_DATA.items()))
        self.assertEquals(app.id, 123)
        self.assertEquals(app.title, 'This is the title')
        self.assertEquals(app.type, 'foo')
        self.assertEquals(app.status, 1)
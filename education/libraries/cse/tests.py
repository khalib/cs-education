import json
from django.test import TestCase
from education.core.utils import json_to_obj
from education.libraries.cse.api import CSEAPI
from education.libraries.cse.user import User
from education.libraries.cse.node.node import Node
from education.libraries.cse.node import Product, Review, Flow, Blog, Board


NODE_DATA = {
    'id': 123,
    'author': {
        'id': 111,
        'first_name': 'Foo',
        'last_name': 'Bar',
        'profile_url': 'http://www.foo.com/user/foo-bar',
    },
    'status': 1,
    'title': 'FooBar',
    'type': 'app',
    'created': '2013-12-12T14:40:02.000Z',
    'changed': '2014-12-12T14:40:02.000Z',
    'url': 'http://www.foo.com/bar-app',
}

PRODUCT_DATA = dict(NODE_DATA.items() +
    {
        'image': 'http://www.foo.com/images/bar.jpg'
    }.items()
)

REVIEW_DATA = dict(NODE_DATA.items() +
    {
        'one_liner': 'Foo bar one liner',
        'url': 'http://www.foo.com/review-foo/bar',
        'learning_rating': 5,
        'author': {
            'id': 111,
            'first_name': 'Foo',
            'last_name': 'Bar',
            'profile_url': 'http://www.foo.com/user/foo-bar',
        },
    }.items()
)


class CSEAPITest(TestCase):
    def test_request(self):
        api = CSEAPI()
        endpoint = '/v3/educator/products'

        # Test invalid auth request.
        data = api.request(endpoint, { 'clientId': 'qwer' })
        self.assertEquals(data.statusCode, 401)

        # Test valid endpoint.
        data = api.request(endpoint)
        self.assertEquals(data.statusCode, 200)
        self.assertIsInstance(data.response, list)

    def test_get_products(self):
        api = CSEAPI()

        # Test for radom products.
        products = api.get_products()
        for product in products:
            self.assertIsInstance(product.id, int)
            self.assertTrue(product.type in ['app', 'website', 'game'])

    def test_get_product_by_slug(self):
        api = CSEAPI()

        # Test for a product by review URL slug.
        slug = 'game/winds-of-orbis'
        product = api.get_product_by_slug(slug)
        self.assertIsInstance(product.id, int)
        self.assertTrue(product.type, 'game')
        self.assertTrue((slug in product.review.url))

    def test_get_product(self):
        api = CSEAPI()

        # Get a product from the products API.
        products = api.get_products()
        product = api.get_product(products[0].id)

        self.assertEquals(product.id, products[0].id)
        self.assertEquals(product.title, products[0].title)
        self.assertEquals(product.type, products[0].type)

    def test_get_user_by_slug(self):
        api = CSEAPI()

        user = api.get_user_by_slug('users/root')
        self.assertIsInstance(user, User)
        self.assertIsInstance(user.id, int)

    def test_get_nodes(self):
        api = CSEAPI()

        # Test various node types.
        nodes = api.get_nodes('flow')
        for node in nodes:
            self.assertEquals(node.type, 'flow')

        nodes = api.get_nodes('blog')
        for node in nodes:
            self.assertEquals(node.type, 'blog')

        nodes = api.get_nodes('board')
        for node in nodes:
            self.assertEquals(node.type, 'board')


class NodeTest(TestCase):
    def test_init(self):
        # Test dictionary to object data conversions.
        data = {
            'foo': 'bar',
            'baz': 'bat',
            'nested': {
                'hello': 'world',
                'child': {
                    'foobar': 'foo',
                }
            },
            'author': {
                'id': 123,
                'first_name': 'John',
                'last_name': 'Doe',
            }
        }

        node = Node(data)
        self.assertEquals(node.foo, 'bar')
        self.assertEquals(node.baz, 'bat')
        self.assertEquals(node.author.id, 123)
        self.assertEquals(node.author.first_name, 'John')
        self.assertEquals(node.author.last_name, 'Doe')
        self.assertEquals(node.nested.child.foobar, 'foo')

    def test_instance(self):
        # Test various instances.
        node = Node.instance('flow', {})
        self.assertIsInstance(node, Flow)

        node = Node.instance('review', {})
        self.assertIsInstance(node, Review)


class UserTest(TestCase):
    def test_init(self):
        data = {
            'id': 123,
            'first_name': 'John',
            'last_name': 'Doe',
            'profile_url': 'http://www.foo.com/user/foo-bar',
            'child': {
                'foo': 'bar',
                'grandchild': {
                    'baz': 'bat',
                }
            }
        }

        user = User(data)
        self.assertEquals(user.id, 123)
        self.assertEquals(user.first_name, 'John')
        self.assertEquals(user.last_name, 'Doe')
        self.assertEquals(user.child.foo, 'bar')
        self.assertEquals(user.child.grandchild.baz, 'bat')
        self.assertEquals(user.profile_url, 'http://www.foo.com/user/foo-bar')


class ProductTest(TestCase):
    def test_product_init(self):
        product = Product(PRODUCT_DATA)
        self.assertEquals(product.id, 123)
        self.assertEquals(product.type, 'app')
        self.assertEquals(product.status, 1)
        self.assertEquals(product.title, 'FooBar')
        self.assertEquals(product.created, '2013-12-12T14:40:02.000Z')
        self.assertEquals(product.changed, '2014-12-12T14:40:02.000Z')
        self.assertEquals(product.author.id, 111)
        self.assertEquals(product.author.first_name, 'Foo')
        self.assertEquals(product.author.last_name, 'Bar')

    def test_get_pricing_summary(self):
        # Test for pricing structure only.
        data = {
            'pricing_structure': [
                { 'name': 'Paid' },
                { 'name': 'Freemium' },
            ]
        }
        product = Product(data)
        summary = product.get_pricing_summary()
        self.assertEquals(', '.join(summary), 'Paid, Freemium')

        # Test for pricing only.
        data = {
            'price': '$19.99',
        }
        product = Product(data)
        summary = product.get_pricing_summary()
        self.assertEquals(', '.join(summary), '$19.99')

        # Test for pricing structure and price.
        data = {
            'price': '$19.99',
            'pricing_structure': [
                { 'name': 'Paid' },
                { 'name': 'Freemium' },
            ]
        }
        product = Product(data)
        summary = product.get_pricing_summary()
        self.assertEquals(', '.join(summary), 'Paid, Freemium, $19.99')

    def test_get_grade_range(self):
        # Test for multiple grades.
        data = {
            'grades': [
                { 'name': 'Pre-K' },
                { 'name': 'K' },
                { 'name': '1' },
                { 'name': '2' },
            ]
        }
        product = Product(data)
        grade_range = product.get_grade_range()
        self.assertEquals(grade_range, 'Pre-K - 2')

        # Test for single grade.
        data = {
            'grades': [
                { 'name': 'Pre-K' },
            ]
        }
        product = Product(data)
        grade_range = product.get_grade_range()
        self.assertEquals(grade_range, 'Pre-K')

class ReviewTest(TestCase):
    def test_get_url_path(self):
        review = Review(REVIEW_DATA)
        self.assertEquals(review.get_url_path(), '/review-foo/bar')
        self.assertEquals(review.one_liner, 'Foo bar one liner')
        self.assertEquals(review.learning_rating, 5)

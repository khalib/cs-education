import urllib, urllib2, json
from django.conf import settings
from education.core.utils import json_to_obj
from education.libraries.cse.node.node import Node
from education.libraries.cse.node import Flow, Review, Product
# from education.libraries.cse.product import Product, App, Website, Game
from education.libraries.cse.user import User


class CSEAPI(object):
    def request(self, endpoint, query_args={}):
        """
        Makes a request to the CSE API.
        """
        query_defaults = {
            'clientId': settings.CSE_API_CLIENT_ID,
            'appId': settings.CSE_API_APP_ID
        }

        query = dict(query_defaults.items() + query_args.items())
        result = urllib2.urlopen('%s%s?%s' % (settings.CSE_API_HOST, endpoint, urllib.urlencode(query)))
        data = result.read()

        return json_to_obj(data)

    def get_products(self, query_args={}):
        """
        Get a list of product data.
        """
        endpoint = '/v3/educator/products'
        result = self.request(endpoint, query_args)

        products = []
        for data in result.response:
            # Dynamically load product instance.
            class_name = data.type.capitalize()
            product = Product.instance(class_name, data)
            products.append(product)

        return products

    def get_product(self, id):
        """
        Get product detail data.
        """
        endpoint = '/v3/educator/products/%s' % id
        result = self.request(endpoint)
        data = result.response

        # Dynamically load product instance.
        class_name = data.type.capitalize()
        product = Product.instance(class_name, data)

        return product

    def get_product_by_slug(self, slug):
        """
        Get product by URL slug.
        """
        return self.get_products({ 'review_url': slug })[0]

    def get_review(self, id):
        """
        Get product review detail data.
        """
        endpoint = '/v3/educator/reviews/%s' % id
        result = self.request(endpoint)

    def get_users(self, query_args={}):
        """
        Get a list of users.
        """
        endpoint = '/v3/educator/users'
        result = self.request(endpoint, query_args)

        users = []
        for data in result.response:
            user = User(data)
            users.append(user)

        return users

    def get_user_by_slug(self, slug):
        """
        Get user details by slug.
        """
        users = self.get_users({ 'profile_url': slug })
        if len(users) > 0:
            return users[0]

    def get_nodes(self, type, query_args={}):
        """
        Get a list of nodes.
        """
        endpoint = '/v3/educator/%ss' % (Node.TYPE_MAP[type])
        result = self.request(endpoint, query_args)

        nodes = []
        for data in result.response:
            node = Node.instance(type, data)
            nodes.append(node)

        return nodes


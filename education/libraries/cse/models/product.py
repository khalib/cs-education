from education.libraries.cse.models.node import Node

class Product(Node):
    def as_object(self):
        """
        Converts json data to a data object.
        """
        super(Product, self).as_object()
        self.image = self.data['image']

        return self

    def get_url(self):
        """
        Get the url of the product.
        """
        return '/products/%s' % self.id

class App(Product):
    True
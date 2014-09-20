from education.libraries.cse.node.node import Node
from education.libraries.cse.node import Review


class Product(Node):
    def __init__(self, data=None):
        super(Product, self).__init__(data)

        # Set user object.
        if hasattr(data, 'review'):
            self.review = Review(data.review)

    @staticmethod
    def instance(class_name, data):
        module = __import__('education.libraries.cse.node.product', {}, {}, class_name)
        Class = getattr(module, class_name)
        instance = Class(data)

        return instance

    def get_pricing_summary(self):
        """
        Generates a list of pricing information.
        """
        summary = []

        if hasattr(self, 'pricing_structure'):
            for pricing in self.pricing_structure:
                summary.append(pricing.name)

        if hasattr(self, 'price'):
            summary.append(self.price)

        return summary

    def get_grade_range(self):
        if hasattr(self, 'grades'):
            if len(self.grades) == 1:
                return self.grades[0].name
            else:
                grade_range = [self.grades[0].name, self.grades[-1].name]
                return ' - '.join(grade_range)


class App(Product):
    pass


class Website(Product):
    pass


class Game(Product):
    pass

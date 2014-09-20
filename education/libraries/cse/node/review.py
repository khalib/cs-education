from urlparse import urlparse
from education.libraries.cse.node.node import Node


class Review(Node):
    def get_url_path(self):
        return urlparse(self.url).path
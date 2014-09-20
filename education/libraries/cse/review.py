from urlparse import urlparse
from education.libraries.cse.node import NodeObject


class Review(NodeObject):
    def get_url_path(self):
        return urlparse(self.url).path
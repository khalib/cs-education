import types, json
from urlparse import urlparse
from education.core.utils import json_to_obj


class User(object):
    def __init__(self, data=None):
        # Set the data attributes to this object.
        if type(data) is types.DictType:
            data = json_to_obj(json.dumps(data))

        for k, v in vars(data).iteritems():
            setattr(self, k, v)

    def get_profile_url_path(self):
        return urlparse(self.profile_url).path
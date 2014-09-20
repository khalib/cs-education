import types, json
from education.core.utils import json_to_obj
from education.libraries.cse.user import User


class NodeObject(object):
    def __init__(self, data=None):
        # Set the data attributes to this object.
        if type(data) is types.DictType:
            data = json_to_obj(json.dumps(data))

        for k, v in vars(data).iteritems():
            setattr(self, k, v)

        # Set user object.
        if hasattr(data, 'author'):
            self.author = User(data.author)

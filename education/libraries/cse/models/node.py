import json

class Node(object):
    def __init__(self, data=None):
        if data:
            self.data = data
            self.as_object()

    def as_object(self):
        self.id = int(self.data['id'])
        self.title = self.data['title']
        self.type = self.data['type']
        self.status = int(self.data['status'])
        self.created = self.data['created']
        self.changed = self.data['changed']

        return self
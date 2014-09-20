import json
from django.test import TestCase
from education.core.utils import json_to_obj


DATA_DICT = {
    'foo': 'bar',
    'baz': 'bat',
    'child': {
        'childfoo': 'childbat',
        'grandchild':  {
            'grandchildfoo': 'grandchildbat',
        }
    },
    'list': [
        { 'id': 1, 'foo': 'bar' },
        { 'id': 2, 'foo': 'baz' },
        { 'id': 3, 'foo': 'foobar' },
    ]
}

class jsonToObjTest(TestCase):
    def test_json_to_obj(self):
        j = json.dumps(DATA_DICT)

        obj = json_to_obj(j)
        self.assertEquals(obj.foo, 'bar')
        self.assertEquals(obj.baz, 'bat')
        self.assertEquals(obj.child.childfoo, 'childbat')
        self.assertEquals(obj.child.grandchild.grandchildfoo, 'grandchildbat')
        self.assertEquals(obj.list[0].foo, 'bar')
        self.assertEquals(obj.list[1].foo, 'baz')
        self.assertEquals(obj.list[2].foo, 'foobar')
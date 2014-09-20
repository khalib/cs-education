import types, json
from collections import namedtuple
from pprint import pprint


def GLog(output, type='output'):
    if type is 'header':
        print('\n')
        print('_' * (output.__len__() + 4))
        print('| ' + ' ' * output.__len__() + ' |')
        print('| ' + output + ' |')
        print('| ' + ' ' * output.__len__() + ' |')
        print('-' * (output.__len__() + 4) + '\n')
    elif type is 'pretty':
        pprint(output)
    else:
        print(output)

def _json_object_hook(d):
    return namedtuple('X', d.keys())(*d.values())

def json_to_obj(data):
    """
    Converts JSON into an object to the nth degree.
    """
    return json.loads(data, object_hook=_json_object_hook)

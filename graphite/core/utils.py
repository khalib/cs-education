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
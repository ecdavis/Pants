''' Compatibility module that helps to resolve some inconsistencies between
    python 2 and 3
'''

def items(mapping):
    ''' returns the dictionary's item view '''
    return getattr(dictionary, 'viewitems', dictionary.items)()

def keys(mapping):
    ''' returns the dictionary's key view '''
    return getattr(dictionary, 'viewkeys', dictionary.keys)()

def values(mapping):
    ''' returns the dictionary's value view '''
    return getattr(dictionary, 'viewvalues', dictionary.values)()

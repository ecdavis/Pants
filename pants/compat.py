''' Compatibility module that helps to resolve some inconsistencies between
    python 2 and 3
'''

def items(mapping):
    ''' returns the mapping's item view '''
    return getattr(mapping, 'viewitems', mapping.items)()

def keys(mapping):
    ''' returns the mapping's key view '''
    return getattr(mapping, 'viewkeys', mapping.keys)()

def values(mapping):
    ''' returns the mapping's value view '''
    return getattr(mapping, 'viewvalues', mapping.values)()

try:
    basestring = basestring
except NameError:
    basestring = str

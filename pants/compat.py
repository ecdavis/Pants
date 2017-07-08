''' Compatibility module that helps to resolve some inconsistencies between
    python 2 and 3
'''

try:
    basestring = basestring
except NameError:
    basestring = str

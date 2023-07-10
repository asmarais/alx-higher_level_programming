#!/usr/bin/python3
'''
a function that returns True if the object is an instance of a class
that inherited (directly or indirectly) from the specified class ; otherwise
 False.
'''


def is_kind_of_class(obj, a_class):
    '''
    checks if an object is an instance of class
    '''
    return isinstance(obj, a_class)

#!/usr/bin/python3
'''function that returns True if the object is an instance of a class
   that inherited (directly or indirectly) from the specified class ;
   otherwise False.
'''


def check_inheritance(obj, parent_class):
    return issubclass(type(obj), parent_class)

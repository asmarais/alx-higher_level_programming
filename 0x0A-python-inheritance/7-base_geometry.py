#!/usr/bin/python3
'''Write an empty class BaseGeometry.'''


class BaseGeometry:
    '''create a class'''

    def area(self):
        '''
        raise an exception
        '''
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
         '''
         validate an integer'''
         if type(value) is not int:
              raise TypeError("{} must be an integer".format(name))
         if value <= 0:
              raise ValueError("{} must be greater than 0".format(name))

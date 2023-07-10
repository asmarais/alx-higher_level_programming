#!/usr/bin/python3
'''7-base_geometry.py'''


class BaseGeometry:
    '''
    class BaseGeometry
    '''

    def __init__(self):
        pass

    def area(self):
        '''
        raise an exception
        '''

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
<<<<<<< HEAD
        validate an integer
        '''

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
=======
        check value input is correct type
        '''
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
>>>>>>> ec093271d25c195436fed64520b904180a2f2031
            raise ValueError("{} must be greater than 0".format(name))

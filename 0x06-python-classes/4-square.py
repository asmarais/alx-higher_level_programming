#!/usr/bin/python3
'''3-square.py: Defines size as an int and also >= 0'''


class Square:
    ''' create a classe called square'''

    def __init__(self, size=0):
        ''' initializes a class'''
        self.__size = size

        @property
        def size(self):
            '''retrievs the size'''
            return self.__size

        @size.setter
        def size(self, size):
            '''sets the size'''
            self.__size = size
            if type(size) is not int:
                raise TypeError('size must be an integer')
            if size < 0:
                raise ValueError('size must be >= 0')

        def area(self):
            '''returns the current square area'''
            return self.__size * self.__size

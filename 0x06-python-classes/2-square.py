#!/usr/bin/python3
'''2-square.py: Defines size as an int and also >= 0'''


class Square:
    ''' create a classe called square'''

    def __init__(self, size=0):
        ''' initializes a class'''
        self.__size = 0
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

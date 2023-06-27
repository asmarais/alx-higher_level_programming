#!/usr/bin/python3
'''0-square.py: Defines a square with a private attribute callsed size'''


class Square:
    '''create a square with a size private attribute'''

    def __init__(self, size):
        '''Intialize a class square with size'''

        self.__size = size

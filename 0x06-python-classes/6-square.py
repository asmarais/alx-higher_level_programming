#!/usr/bin/python3
'''5-square.py: Defines size as an int and also >= 0'''


class Square:
    ''' create a classe called square'''

    def __init__(self, size=0, position=(0, 0)):
        ''' initializes a class'''
        self.__size = size
        try:
            self.position = position
        except TypeError as typ:
            print(typ)

    @property
    def position(self):
        '''retrieves the position'''
        return self.__position

    @position.setter
    def position(self, value):
        '''sets the valuse of position'''
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(num, int) for num in value) or \
                not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    @property
    def size(self):
        '''retrievs the size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''sets the size'''
        self.__size = value
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        '''returns the current square area'''
        return self.__size * self.__size

    def my_print(self):
        '''prints a square with'#' '''
        if self.__size == 0:
            print()
        else:
            print('\n' * self.position[1], end="")
            for a in range(self.__size):
                print(" " * self.position[0] + "#" * self.size)

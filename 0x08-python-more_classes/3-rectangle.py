#!/usr/bin/python3
'''3-rectangle.py: that defines a rectangle and a perimeter'''


class Rectangle:
    '''Defines the Rectangle type'''

    def __init__(self, width=0, height=0):
        '''Initialize a class Rectangle'''

        self.width = width
        self.height = height

    @property
    def width(self):
        '''sets the width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''sets the width'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''sets the height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''sets the height'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return self.__height * 2 + self.__width * 2

    def area(self):
        return self.__height * self.__width

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        for h in range(self.__height):
            for w in range(self.height - 1):
                print('#' * self.__width)
            return '#' * self.width

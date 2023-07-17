#!/usr/bin/python3

'''Square class module'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square class attributes'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Instantiation of Square attriutes'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''print attribute with __str__'''
        a, b, c, d = self.id, self.x, self.y, self.size
        return ("[Square] ({}) {}/{} - {}".format(a, b, c, d))

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''Set up args for rectangle'''
        if len(args) != 0:
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.id = args[0]
                self.size = args[1]
            if len(args) == 3:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
            if len(args) == 4:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
        else:
            for key, values in kwargs.items():
                setattr(self, key, values)

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

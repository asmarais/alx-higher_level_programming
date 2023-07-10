#!/usr/bin/python3
'''
a class MyList that inherits from list
'''


class MyList(list):
    '''print the elements of the list in an ascending sort'''
    def print_sorted(self):
        new = sorted(self)
        print(new)

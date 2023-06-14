#!/usr/bin/python3
def uniq_add(my_list=[]):
    s = set(my_list)
    sum = 0
    for element in s:
        sum += element
    return sum

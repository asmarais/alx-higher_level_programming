#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a is None or tuple_b is None:
        return
    new_a = tuple_a + (0, 0)
    new_b = tuple_b + (0, 0)
    a = new_a[0] + new_b[0]
    b = new_a[1] + new_b[1]
    return (a,b)

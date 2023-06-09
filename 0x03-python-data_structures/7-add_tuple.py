#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    a = 0
    b = 0
    if len_a == 0:
        if len_b == 1:
            a = tuple_b[0]
        elif len_b == 2:
            a = tuple_b[0]
            b = tuple_b[1]
    elif len_a == 1:
        a = tuple_a[0]
        if len_b == 1:
            a += tuple_b[0]
        elif len_b == 2:
            a += tuple_b[0]
            b = tuple_b[1]
    else:
        a = tuple_a[0]
        b = tuple_a[1]
        if len_b == 1:
            a += tuple_b[0]
        elif len_b == 2:
            a += tuple_b[0]
            b += tuple_b[1]
    return (a,b)

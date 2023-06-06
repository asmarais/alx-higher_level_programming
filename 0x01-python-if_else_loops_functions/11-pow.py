#!/usr/bin/python3
def pow(a, b):
    p = 1
    if b < 0:
        for i in range(-b):
            p = p * 1 / a
    for i in range(b):
        p = p * a
    return(p)

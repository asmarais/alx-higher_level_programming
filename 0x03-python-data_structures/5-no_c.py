#!/usr/bin/python3
def no_c(my_string):
    length = len(my_string)
    s = ""
    for alph in my_string:
        if alph == 'c' or alph == 'C':
            continue
        else:
            s += alph
    return s

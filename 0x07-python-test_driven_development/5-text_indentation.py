#!/usr/bin/python3


'''
   5-text_indentation. function

   a function that prints a text with 2 new lines
'''


def text_indentation(text):
    '''
    Python function that prints a text with 2 new lines
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ['.', '?', ':']
    lines = []
    line = ''

    for char in text:
        line += char
        if char in separators:
            lines.append(line.strip())
            line = ''

    if line:
        lines.append(line.strip())

    for i in range(len(lines)):
        print(lines[i])
        if i == len(lines)-1:
            print(lines[i], end="")

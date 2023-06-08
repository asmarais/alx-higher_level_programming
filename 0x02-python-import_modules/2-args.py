#!/usr/bin/python3
import sys
arguments = sys.argv
if __name__ == "__main__":
    if (len(arguments) == 2):
        print("1 argument:")
        print("1: {}".format(arguments[1]))
    else:
        if (len(arguments) == 1):
            print("0 arguments.")
        else:
            print("{} arguments:".format(len(arguments) - 1))
            for index in range(1, len(arguments)):
                print("{}: {}".format(index, arguments[index]))

#!/usr/bin/python3
from sys import argv
pos = 1
if __name__ == '__main__':
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        print("1 argument:")
        print("1: {}".format(len(argv[1])))
    else:
        args = len(argv) - 1
        print('{} arguments: '.format(args))    
        while (args >= pos):
            print('{:d}: {:s}'.format(pos, argv[pos]))
            pos += 1

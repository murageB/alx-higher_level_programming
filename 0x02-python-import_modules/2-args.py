#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    args = len(sys.argv) - 1
    print('{} arguments: '.format(args))
    pos = 1
    while (args >= pos):
        print('{}: {}'.format(pos, sys.argv[pos]))
        pos += 1

#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv
    length = len(argv)

    if length == 1:
        print("{} arguments.".format(length - 1))
    elif length == 2:
        print("{} argument:\n{}: {}".format(length - 1,
              length - 1, argv[length - 1]))
    else:
        for x in range(length - 1):
            print("{} arguments:\n{}: {}".format(length - 1,
                  x + 1, argv[x + 1]))

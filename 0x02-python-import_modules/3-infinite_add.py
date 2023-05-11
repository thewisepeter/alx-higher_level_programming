#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv
    length = len(argv)
    sum = 0
    for x in range(length - 1):
        argv[x + 1] = int(argv[x + 1])
        sum += argv[x + 1]
    print("{}".format(sum))

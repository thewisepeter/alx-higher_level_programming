#!/usr/bin/python3
"""prints the ASCII alphabet, in reverse order
alternating lowercase and uppercase"""

for char in range(90, 64, -1):
    if char % 2 == 0:
        char += 32
    print("{}".format(chr(char)), end="")

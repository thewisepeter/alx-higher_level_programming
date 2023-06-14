#!/usr/bin/python3
"""module that inserts a line of text to a file,
    after each line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each line
        containing a specific string"""
    with open(filename, encoding='utf-8') as f:
        content = f.readlines()
        f.seek(0)
        for line in content:
            f.write(line)
            if search_string in line:
                f.write(new_string + '\n')

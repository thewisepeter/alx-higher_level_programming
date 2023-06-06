#!/usr/bin/python3
"""module that prints a text with 2 new lines after each
    of these characters: ., ? and :"""


def text_indentation(text):
    """function that prints a text with 2 new lines
    after each of these characters: ., ? and :"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars = [".", "?", ":"]
    result = ""
    lines = text.splitlines()

    for line in lines:
        line = line.strip()
        if line:
            for char in chars:
                line = line.replace(char, char + "\n\n")
        result += line + "\n"

    print(result[:-1])

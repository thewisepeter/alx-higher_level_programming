#!/usr/bin/python3
def roman_to_int(roman_string):
    """function that converts a Roman numeral to an integer"""
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    result = 0
    previous_value = 0

    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                    'C': 100, 'D': 500, 'M': 1000}
    for char in roman_string:
        value = roman_values.get(char, 0)
        result += value

        if value > previous_value:
            result -= 2 * previous_value

        previous_value = value

    return result

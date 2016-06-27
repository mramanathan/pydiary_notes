"""
Validation Exercises

These functions return ``True`` or ``False`` depending on whether the
string passes a condition.

"""

import re

def has_vowel(string):
    result = bool(re.search(r'[aeiou]', string))
    if result:
        return True
    else:
        return False
    """Return True iff the string contains one or more vowels."""


def is_integer(string):
    result = bool(re.search(r'^[+-]{0,1}\d+$', string))
    if result:
        return True
    else:
        return False
    """Return True iff the string represents a valid integer."""


def is_fraction(string):
    """Return True iff the string represents a valid fraction."""


def is_valid_date(string):
    """Return True iff the string represents a valid YYYY-MM-DD date."""


def is_number(string):
    #result = bool(re.search(r'^\W{1}\d*\W{1}\d*$', string))
    result = bool(re.search(r'^[+-.]{0,1}\d*[.]\d+$', string))
    if result:
        return True
    else:
        return False
    """Return True iff the string represents a decimal number."""


def is_hex_color(string):
    """Return True iff the string represents an RGB hex color code."""

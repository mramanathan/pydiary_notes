"""
Substitution Exercises

These functions return a new altered version of the given string.

"""

import re

def get_extension(filename):
    result = re.search(r'\.\w+$', filename)
    return result.group().split('.')[1]
    """Return the file extension for a full file path."""


def normalize_jpeg(filename):
    if "JPEG" in filename:
        newname = re.sub("JPEG", "jpg", filename)
        return newname
    if "jpeg" in filename:
        newname = re.sub("jpeg", "jpg", filename)
        return newname
    if "Jpg" in filename:
        newname = re.sub("Jpg", "jpg", filename)
        return newname
    if "gif" in filename:
        return filename
    """Return the filename with jpeg extensions normalized."""


def normalize_whitespace(string):
    newstr = re.sub("\s+", " ", string)
    return newstr
    """Replace all runs of whitespace with a single space."""


def compress_blank_lines(string, max_blanks):
    """Compress N or more empty lines into just N empty lines."""


def normalize_domain(string):
    if "http://www:" in string:
        print "gotcha"
        #temp = re.split("[w]{3}\.", string)
        #result = "https://" + temp[1]
        #return result
    elif "http://treyhunner" in string:
        result = re.sub("http:", "https:", string)
        return result
    elif "https" in string:
        return string
    else:
        return string
    """Normalize all instances of treyhunner.com URLs."""


def convert_linebreaks(string):
    """Convert linebreaks to HTML."""

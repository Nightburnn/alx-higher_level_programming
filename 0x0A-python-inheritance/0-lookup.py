#!/usr/bin/python3

def lookup(obj):
    """Get a list of the objects's attributes and methods"""

    attributes = dir(obj)
    return attributes

#!/usr/bin/python3
""" this is my add_integer module """


def add_integer(a, b=98):
    """Function that returns the addition of a + b

    Args:
        a: should be an int. if not throw error
        b: second int. if not throw error. default val is 98.

    Returns:
        The addition of a + b or a raised TypeError
    """
    if type(a) is int or type(a) is float:
        if type(b) is int or type(b) is float:
            return int(a + b)
        else:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("a must be an integer")

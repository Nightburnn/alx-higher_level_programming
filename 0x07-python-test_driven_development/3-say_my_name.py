#!/usr/bin/python3
""" function that prints a string """


def say_my_name(first_name, last_name=""):
    """ prints out My name is <first name> <last name>

    Args:
        first_name: nombre
        last_name: apellido

    Return: returns a string or a thype error
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

#!/usr/bin/python3
""" function that prints a text with new lines """


def text_indentation(text):
    """ After each . ? and : print 2 new lines

    Args:
        text: the wall of text that we are given

    Return: none, just print
    """
    last = " "
    string = ""
    if text is "":
        print(string, end='')
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in text:
        if i is last and i is ' ':
            last = i
            continue
        if (last is '.' or last is '?' or last is ':') and i is ' ':
            last = i
            continue
        if i is '.' or i is '?' or i is ':':
            string += i + "\n" + "\n"
            last = i
        else:
            string += i
            last = i
    print(string.rstrip(' '), end="")

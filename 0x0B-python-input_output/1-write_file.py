#!/usr/bin/python3
"""Create a UTF-8 text file and write a string to it"""


def write_file(filename="", text=""):
    """Create a text file and write a string to it.
    Args:
    filename (str): The name of the file to create.
    text (str): The text to write to the file.
    Returns:
    The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

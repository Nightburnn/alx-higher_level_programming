#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):

    """Create a copy of the list and sort it in ascending order"""

    def print_sorted(self):

        """Print the sorted list"""

        print(sorted(self))

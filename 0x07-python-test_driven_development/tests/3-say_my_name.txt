"""
TEST CASES FOR NOMBRES AN APELLIDO
"""

>>> say_my_name = __import__('3-say_my_name').say_my_name

>>> say_my_name("John", "Smith")
My name is John Smith

>>> say_my_name("Groot")
My name is Groot 

>>> say_my_name("")
My name is  


>>> say_my_name("", "")
My name is  

""" ERRORS """


>>> say_my_name(3, "White")
Traceback (most recent call last):
...
TypeError: first_name must be a string


>>> say_my_name("Walter", 3)
Traceback (most recent call last):
...
TypeError: last_name must be a string


>>> say_my_name(, )
Traceback (most recent call last):
...
SyntaxError: invalid syntax


>>> say_my_name( )
Traceback (most recent call last):
...
TypeError: say_my_name() missing 1 required positional argument: 'first_name'

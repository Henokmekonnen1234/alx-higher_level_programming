#!usr/bin/python3
""" Square class is a class which have size attribute
        with private instance attribute
"""


class Square:
    """ Square class is a class which have size attribute
         with private instance attribute
    """

    def __init__(self, size=0):
        """ the __init__ method is special type of method
             which it intialize the fields of the class

             Args:
                 size : int
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

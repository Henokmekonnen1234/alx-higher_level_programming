#!usr/bin/python3
class Square:
    """ Square class is a class which have size attribute
        with private instance attribute

        Attribute
        ---------
        size : int
            value of length of sides
        """

    def __init__(self, size):

        """ the __init__ method is special type of method
            which it intialize the fields of the class

            Attributes
            ----------
            size : int
                it holds the length of the values
            Return
            ------
            no value to return """
        self.__size = size

#!usr/bin/python3
""" Square class is a class which have size attribute
    with private instance attribute """


class Square:
     """ Square class is a class which have size attribute
		 with private instance attribute """

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

#!/usr/bin/python3
"""
Module square.py

This module described below
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """ initialises the value

        Args:
            size (any): the length of the side
            x (any): the x coordinate
            y (any): the y coordinate
            id (any):  the unique identifier of the object
        """
        self.size = size
        super().__init__(self.size, self.size, x, y, id)

    @property
    def size(self):
        """getter method for size

        Returns:
            int: the legth of the side
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter method for size

        Args:
            value (any): it could be an value
        """
        self.validate_all("width", value)
        self.__size = value
        self.width = self.height = self.__size

    def update(self, *args, **kwargs):
        """update the instances with the new value

        Args:
            args (tuples): they are lists of new values
            kwargs (dict): they are key-value pair of the new value
        """
        if len(args) > 0:
            for k, v in enumerate(args):
                if k == 0:
                    self.id = v
                elif k == 1:
                    self.size = v
                elif k == 2:
                    self.x = v
                elif k == 3:
                    self.y = v
        else:
            if "id" in kwargs.keys():
                self.id = kwargs["id"]
            if "size" in kwargs.keys():
                self.size = kwargs["size"]
            if "x" in kwargs.keys():
                self.x = kwargs["x"]
            if "y" in kwargs.keys():
                self.y = kwargs["y"]

    def to_dictionary(self):
        """store the values to dictionary mode

        Returns:
            dict: dictionnary represetation of the class
        """
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }

    def __str__(self):
        """returns when the class is called

        Returns:
            [Square]({id}){x}/{y}-{width}/{height}: this will be shown
            """
        return f"[{self.__class__.__name__}] ({self.id}) {self.x}/"\
            f"{self.y} - {self.width}"

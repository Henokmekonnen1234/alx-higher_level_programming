#!/usr/bin/python3
"""
Module rectangle.py

This module will be described below
"""

from models.base import Base


class Rectangle(Base):
    """this class inherits from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """this method initializes the values

        Args:
            width (int): side length of the rectangle
            height (int): side length of the rectangle
            x (int): side lengtth of the rectangle
            y (int): side length of the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """this method returns the update value of width

        Returns:
            int: returns the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter method which assignes the value to the width instance

        Args:
            value (any): the length of the side
        """
        self.validate_all("width", value)
        self.__width = value

    @property
    def height(self):
        """this method returns the update value of height

        Returns:
            int: returns the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter method which assignes the value to the width instance

        Args:
            value (any): the length of the side
        """
        self.validate_all("height", value)
        self.__height = value

    @property
    def x(self):
        """this method returns the update value of x

        Returns:
            int: returns the x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter method which assignes the value to the x instance

        Args:
            x (any): the length of the side
        """
        self.validate_all("x", value)
        self.__x = value

    @property
    def y(self):
        """this method returns the update value of y

        Returns:
            int: returns the y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter method which assignes the value to the y instance

        Args:
            y (any): the length of the side
        """
        self.validate_all("y", value)
        self.__y = value

    def validate_all(self, name, value):
        """this method validates all requirement

        Args:
            name (str): the name of the variable
            value (any): it can be any value and it will be examined

        Raises:
            TypeError: if value is different from integer
            ValueError: if value is less than 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif name == "width" or name == "height":
            if value <= 0:
                raise ValueError(f"{name} must be > 0")
        elif name == 'x' or name == 'y':
            if value < 0:
                raise ValueError(f"{name} must be >= 0")

    def area(self):
        """this method will calculate the area of the rectangle

        Returns:
            int: the area of the rectangle
        """
        return (self.__width * self.__height)

    def display(self):
        """this method will display the area using this char  '#'"""
        for i in range(self.y):
            print("")
        for i in range(self.height):
            for k in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print('#', end="")
            print()

    def __str__(self):
        """this method returned when the class it self called

        Returns:
            str: string representation of the class
        """
        return f"[{self.__class__.__name__}] ({self.id}) "\
            f"{self.__x}/{self.__y} - {self.__width}"\
            f"/{self.__height}"

    def update(self, *args, **kwargs):
        """update the instances with the new value"""
        if args is not None and len(args) > 0:
            for i, value in enumerate(args):
                if i == 0:
                    self.id = value
                elif i == 1:
                    self.width = value
                elif i == 2:
                    self.height = value
                elif i == 3:
                    self.x = value
                elif i == 4:
                    self.y = value
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """store the values to dictionary mode

        Returns:
            dict: dictionnary represetation of the class
        """
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }

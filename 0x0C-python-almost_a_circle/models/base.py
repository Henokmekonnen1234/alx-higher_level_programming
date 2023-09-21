#!/usr/bin/python3
"""
Module base.py

This module will be described below
"""

import json
import turtle
import csv
import os


class Base:
    """ Base class will be described

    Attributes:
        __nb_objects (int): private class instant
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """this method initializes the values

        Args:
            id (int): we assign it to the values
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """this method will serilizes the list

        Args:
            list_dictionaries (list): list of instaces

        Returns:
            str: it will serilizes and return str representation of list
        """
        if list_dictionaries is None:
            return "[]"
        elif hasattr(list_dictionaries[0], "to_dictionary"):
            return json.dumps([obj.to_dictionary() for
                              obj in list_dictionaries])
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """this method will save the dict  as json file

        Args:
            list_objs (list): instances of inherited class
        """
        filename = f"{cls.__name__}.json"
        if list_objs is None:
            list_objs = []
        with open(filename, "a", encoding="UTF-8") as jfile:
            jfile.write(cls.to_json_string(list_objs))

    def from_json_string(json_string):
        """this method chages json files to list

        Args:
            json_string (str): json file

        Returns:
            list: returns the list changed from json file
        """
        if json_string is None:
            return []
        else:
            return list(json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """this method create and set the instances of the classes

        Args:
            dictionary (dict): contain the values of the instance

        Returns:
            instaces of the classes
        """
        dummy = cls(111, 123)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """it read from files

        Returns:
            list of istances
        """
        list_of_instance = []
        try:
            with open(f"{cls.__name__}.json", "r", encoding="UTF-8") as jfile:
                jf = cls.from_json_string(jfile.read())
                for i in jf:
                    list_of_instance.append(cls.create(**i))
            return list_of_instance
        except Exception:
            return list_of_instance
   
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """this method will save the datas in csv file

        Args:
            list_objs (list): contain list of datas
        """
        to_dict = []
        if list_objs is None:
            to_dict = []
        elif hasattr(list_objs[0],"to_dictionary"):
            to_dict = [obj.to_dictionary() for obj in list_objs]
        else:
            to_dict = list_objs
        with open(f"{cls.__name__}.csv", "a+", newline="") as cfile:
            if to_dict is not None:
                writer = csv.DictWriter(cfile, to_dict[0].keys())
                if os.path.getsize(f"{cls.__name__}.csv") == 0:
                    writer.writeheader()
                for value in to_dict:
                    writer.writerow(value)

    @classmethod
    def load_from_file_csv(cls):
        """this method will assign values for the classes from
            the csv file

        Returns:
            list: contain lists of classes
        """
        try:
            ins_list = []
            with open(f"{cls.__name__}.csv", newline="") as cfile:
                reader = csv.DictReader(cfile)
                for row in reader:
                    new_value = {k:int(v) for k, v in row.items()}
                    ins_list.append(cls.create(**new_value))
        except FileNotFoundError as e:
            print(e)
            ins_list = []
        except Exception as e:
            print(e)
            ins_list =  []
        return ins_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """this method will draw the Rectanle and Square at given size"""
        color_list = [
            "#FF0000",
            "#0000FF",
            "#00FF00",
            "#FFFF00",
            "#FFA500",
            "#800080",
            "#FFC0CB",
            "#8B4513",
            "#000000",
            "#FFFFFF",
            "#808080",
            "#00FFFF",
            "#FF00FF",
            "#E6E6FA",
            "#008080",
            "#F5F5DC",
            "#FFD700",
            "#C0C0C0",
            "#4B0082",
            "#800000",
            "#40E0D0",
            "#808000",
            "#FF7F50",
            "#708090",
            "#CCCCFF"]
        turtle.title("Rectangles and Squares")
        t = turtle.Turtle()
        t.color(random.choice(color_list), random.choice(color_list))
        t.penup()
        t.goto(100, 350)
        t.pendown()
        t.write("0x0C. Python - Almost a circle project", align="center",
                font=("Arial", 30, "normal"))
        if list_rectangles is not None and list_squares is not None:
            for rectangle in list_rectangles:
                rct = rectangle
                t.color(random.choice(color_list), random.choice(color_list))
                t.penup()
                t.goto(rct.x * 4, rct.y * 4)
                t.pendown()
                t.begin_fill()
                t.forward(rct.width)
                t.left(90)
                t.forward(rct.height)
                t.left(90)
                t.forward(rct.width)
                t.left(90)
                t.forward(rct.height)
                t.end_fill()
            t.clear()
            for square in list_squares:
                sq = square
                t.color(random.choice(color_list), random.choice(color_list))
                t.penup()
                t.goto(sq.x * 4, sq.y * 4)
                t.pendown()
                t.begin_fill()
                t.forward(sq.size)
                t.left(90)
                t.forward(sq.size)
                t.left(90)
                t.forward(sq.size)
                t.left(90)
                t.forward(sq.size)
                t.end_fill()
            t.clear()
            t.penup()
            t.goto(0, 0)
            t.pendown()
            t.write("Thank you for your time",align="center",
                     font=("Arial", 30, "normal"))
            turtle.mainloop()
            turtle.done
        else:
            t.penup()
            t.goto(0, 0)
            t.pendown()
            t.write("Sorry there is nothing to show, Thank you for your "
                "time",align="center", font=("Arial", 30, "normal"))
            turtle.done

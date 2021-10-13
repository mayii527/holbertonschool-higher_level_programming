#!/usr/bin/python3
"""
Write a class Student
"""


class Student:
    """attributes"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list:
            dictio = {}
            for i in attrs:
                if i in self.__dict__:
                    dictio[i] = self.__dict__[i]
            return dictio
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for key, value in json():
            self.__dict__[key] = value

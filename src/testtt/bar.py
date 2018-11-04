# coding: utf-8
# Created on: 31.10.2018
# Author: ahw7rng
# E-mail: bosch
"""
Example class for testing

This module illustrates how to document various
Python objects
"""

class Shape(object):
    """
    A very simple class

    This example illustrates writing docstrings for a class.

    :param object: a object as argument

    Example::

        sh = Shape(2,3)
    """
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def area(self):
        """
        Get shape area

        This is an example of a method docstring

        :return: shape area
        :rtype: float
        """
        return self.x * self.y
    def perimeter(self):
        """
        Get shape perimeter

        This is an example of a method docstring

        :return: shape perimeter
        :rtype: float
        """
        return 2 * self.x + 2 * self.y
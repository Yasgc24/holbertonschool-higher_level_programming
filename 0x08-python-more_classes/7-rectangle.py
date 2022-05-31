#!/usr/bin/python3
"""
7. Change representation
"""


class Rectangle:
    """
    Class Rectangle that defines a rectangle
    ----------------------------------------
    Create public class attribute number_of_instances
    ------------------------------------------------
    Create public class attribute print_symbol
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Private instance attribute: width
        Private instance attribute: height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        property to retrieve the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        property setter to set the value of the width
        """
        if not type(value) == int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        property to retrieve the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        property setter to set the value of the height
        """
        if not type(value) == int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Public instance method that
        returns the rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Public instance method that
        returns the rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        print the rectangle with the character #
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rectangle = ""
            for i in range (self.__height):
                if i == self.__height - 1:
                    rectangle += self.__width * str(self.print_symbol)
                else:
                    rectangle += self.__width * str(self.print_symbol) + '\n'
            return rectangle

    def __repr__(self):
        """
        return a string representation of the rectangle
        to be able to recreate a new instance
        """
        width = str(self.__width)
        height = str(self.__height)
        return "Rectangle(" + width + ", " + height + ")"

    def __del__(self):
        """
        Print a message when an instance of Rectangle is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

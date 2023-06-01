import math

class line:
    """
    A class representing a line with width and height.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a line object with given width and height.

        Parameters:
        - width (float or int): The width of the line (default: 0).
        - height (float or int): The height of the line (default: 0).
        """
        self.__width = width
        self.__height = height

    def set_length(self, width, height):
        """
        Set the width and height of the line.

        Parameters:
        - width (float or int): The new width of the line.
        - height (float or int): The new height of the line.
        """
        self.__width = width
        self.__height = height

    def get_length(self):
        """
        Get the width and height of the line.

        Returns:
        - tuple: A tuple containing the width and height of the line.
        """
        return self.__width, self.__height

def area_rectangle(width, height):
    """
    Calculate the area of a rectangle.

    Parameters:
    - width (float or int): The width of the rectangle.
    - height (float or int): The height of the rectangle.

    Returns:
    - float: The calculated area of the rectangle.

    Raises:
    - ValueError: If either width or height is less than or equal to zero.
    """
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive.")
    return width * height

def area_ellipse(width, height):
    """
    Calculate the area of an ellipse.

    Parameters:
    - width (float or int): The major axis (width) of the ellipse.
    - height (float or int): The minor axis (height) of the ellipse.

    Returns:
    - float: The calculated area of the ellipse.

    Raises:
    - ValueError: If either width or height is less than or equal to zero.
    """
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive.")
    return (width * height) * math.pi

def area_right_triangle(width, height):
    """
    Calculate the area of a right triangle.

    Parameters:
    - width (float or int): The base width of the triangle.
    - height (float or int): The height of the triangle.

    Returns:
    - float: The calculated area of the right triangle.

    Raises:
    - ValueError: If either width or height is less than or equal to zero.
    """
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive.")
    return (width * height) / 2
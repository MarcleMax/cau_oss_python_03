import math

class line:
# class 'line' is to generate the value of a line, preparing for the next operations
# as a class, it's better to be named as 'Line' but we just ignore it here
	def __init__(self, length=0):
	# the initial value of the line is zero
		self.__length = length

	def set_length(self, length):
	# set_length is to set the value of the line
		self.__length = length

	def get_length(self):
	# get_length is to get the value of the line for calculating later
		return self.__length

def area_square(length):
# area_square is to calculate: the area of a square, formed by the line we input as sides
	return length ** 2

def area_circle(length):
# area_circle is to calculate: the area of a circle, formed by the line we input as radius
	return length ** 2 * math.pi

def area_regular_triangle(length):
# area_regular_triangle is to calculate: the area of a regular triangle, formed by the line we input as sides
	return length ** 2 * (math.sqrt(3) / 4)
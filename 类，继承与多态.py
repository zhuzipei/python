对#象：id、数据域、方法。类描述对象。
import math


class Circle:

	def __init__(self,radius=1):
		self.__radius = radius

	def get_radius(self):
		return self.__radius

	def get_perimeter(self):
		return 2*self.__radius*math.pi

    def get_area(self):
    	return self.__radius**2*math.pi

    def set_radius(self,radius):
    	self.__radius = radius
#_约定俗成，__事实上可以用'_Circle__radius'修改，不安全。
#对象：id、数据域、方法。类描述对象。
import math
from GeometricObject import GeometricObject

class Circle(GeometricObject):

    __slots__ = 'radius'

	def __init__(self,radius=1):
        super().__init__()
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
#object类：万类之祖。
__new__()
__init__()
__str__()
__eq__(other)#相当于'=='

if isinstance(a,Circle):

dir()#返回所有属性和方法
hasattr(obj, 'power')
setattr(obj, 'y', 19)
getattr(obj, 'y',404)#不存在则返回404
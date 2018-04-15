class Student():
	def __init__(self,name):
		self.name = name

a = Student("Sam")
print a.name

b = Student("UDAY")
print b.name

print "New Example"

class Rectangle():
	def __init__(self,l,b):
		self.length = l
		self.breadth = b
	def getArea(self):
		return self.length*self.breadth
	def getPerimeter(self):
		return 2*(self.length+self.breadth)
a = Rectangle(2,4)
print a.getArea()
print a.getPerimeter()



print "New Example"


class Child():
	def __init__(self,name):
		self.name = name
class Student(Child):
	def __init__(self,name,roll):
		self.roll = roll
		Child.__init__(self,name)
a = Child("xyz")
print a.name
b = Student("abc",12)
print b.name
print b.roll


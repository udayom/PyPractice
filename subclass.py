class Child():
	def __init__(self,name):
		self.name = name
class Student(Child):
	pass
a = Child("xyz")
print a.name
b = Student("abc")
print b.name


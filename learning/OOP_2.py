class Circle():

	pi = 3.14

	def __init__(self, radius = 1):
		self.radius = radius

	def area(self):
		return self.radius * self.radius * self.pi

	def circumfrence(self):
		return 2 * self.pi * self.radius

my_circle = Circle(10)
print(my_circle.radius)
print(my_circle.area())
print(my_circle.circumfrence())

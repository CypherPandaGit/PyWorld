class Animal():

	def __init__(self):
		print('Animal created!')

	def report(self):
		print('Animal')

	def eat(self):
		print('Eating')

class Dog(Animal):

	def __init__(self):
		Animal.__init__(self)
		print('Dog created')

	def report(self):
		print("I'm a dog")

d = Dog()
d.eat()
d.report()

a = Animal()
a.eat()
a.report()

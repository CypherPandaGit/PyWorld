# class NameOfClass():

#     def __init__(self, param1, param2):
#         self.param1 = param1
#         self.param2 = param2

#     def some_method(self):
#         # perform some action
#         print(self.param1)


class Dog():

	# CLASS OBJECT ATTRIBUTES
	species = 'mammal - dog'

	def __init__(self,breed,name):
		self.breed = breed
		self.name = name

sam = Dog('Huskie', 'Sammy')
jim = Dog('Bulldog', 'Jimmie')


class Cat():

	species = 'mammal - cat'

	def __init__(self,breed,name):
		self.breed = breed
		self.name = name

ogie = Cat('Angora', 'Olie')

print(type(sam.breed))
print(sam.breed,sam.name)
print(sam.species)

print(jim.name,jim.breed,jim.species)

print(ogie.name,ogie.breed,ogie.species)
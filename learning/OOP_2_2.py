class Book():
	def __init__(self, title, author, pages):
		self.title = title
		self.author = author
		self.pages = pages

	def __repr__(self):

		return f"Title: {self.title}, Author: {self.author}"


my_book = Book("Python Rocks!", 'Jose', 250)
print(my_book)

#number = "9,223;372:036 854,775;807"
number = input("Please enter a series of numbers, using any separators: ")
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char

print("Separators are separated: " + separators + "\n")

values = "".join(char if char not in separators else " " for char in number).split()

#print(sum([int(val) for val in values]))
print([int(val) for val in values])
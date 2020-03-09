# ip_address = input("Please input an IP address: ")
# print(ip_address.count("."))


parrot_list = ["non pinin", "no more", "a stiff", "bereft of live"]

print("This parrot is ...")
print("What you want to add? ")
# parrot_list.append(input())

for state in parrot_list:
    print("This parrot is " + state)

print("---------------------------------")
print("---------------------------------")

even = [2, 4, 6, 8, 10]
odd = [1, 3, 5, 7, 9]
print("Even numbers: {}".format(even))
print("Odd numbers: {}".format(odd))
numbers = even + odd
print("Merged: {}".format(numbers))

print("--------------")
print("len()")
print(len(numbers))

print("--------------")
print("print(sorted(numbers))") # Not permanently sorted in numbers
print(sorted(numbers))

print("numbers_in_order = sorted(numbers)") # Not permanently sorted too
numbers_in_order = sorted(numbers)
print(numbers_in_order)

print("numbers.sort()") # Permanently sorted in numbers
numbers.sort()
print(numbers)

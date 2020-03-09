# ip_address = input("Please input an IP address: ")
# print(ip_address.count("."))


parrot_list = ["non pinin", "no more", "a stiff", "bereft of live"]

print("This parrot is ...")
print("What you want to add? ")
# parrot_list.append(input())

for state in parrot_list:
    print("This parrot is " + state)

print("-------------")
even = [2, 4, 6, 8, 10]
odd = [1, 3, 5, 7, 9]
print(even)
print(odd)
numbers = even + odd
print(numbers)

print("--------------")
print("len()")
print(len(numbers))

print("--------------")
print("print(sorted(numbers))")
print(sorted(numbers))

print("numbers_in_order = sorted(numbers)")
numbers_in_order = sorted(numbers)
print(numbers_in_order)

print("numbers.sort()")
numbers.sort()
print(numbers)

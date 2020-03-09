my_list = ["audi", "bmw", "mazda", "jaguar", "porsche", "tesla"]

car = iter(my_list)

for item in range(0, len(my_list)):
    print(next(car))

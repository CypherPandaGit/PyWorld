def menu():
    print("Please use options from the list below:")
    print("\t1: Learn Python")
    print("\t2: Learn Java")
    print("\t3: Go swimming")
    print("\t4: Have dinner")
    print("\t5: Go to bed")
    print("\t0: Exit")

choice = "-"
while True:

    if choice == "0":
        break
    elif choice in "12345":
        print("You chose {}".format(choice))
    else:
        menu()

    choice = input()
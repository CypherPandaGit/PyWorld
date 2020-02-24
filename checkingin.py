words = "Hauptstadt Wien"

letter = input("Enter a character: ")

if letter in words:
    print("Yes, '{0}' is in '{1}'.".format(letter, words))
else:
    print("No, '{0}' is not in '{1}'.".format(letter, words))

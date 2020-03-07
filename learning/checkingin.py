words = "Hauptstadt Wien"

letter = input("Enter a character: ")

if letter.casefold() in words.casefold():
    print("Yes, '{0}' is in '{1}'.".format(letter, words))
else:
    print("No, '{0}' is not in '{1}'.".format(letter, words))
low = 1
high = 1000

print("Please think of a numberbetween {0} and {1}: ".format(low,high))
input("Press ENTER key to start")

guesses = 1
while True:
    guesses = low + (high - low) // 2
    high_low = input("My guess is {}. Should i guess higher or lower? "
                     "Enter h or l, or c if my guess was correct"
                     .format(guesses)).casefold()

    if high_low == "h":
        # Guess higher. The low end of the range becomes 1 greater than the guess.

    elif high_low == "l":
        # Guess lower. The high end of the range becomes one less than the guess.

    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))

    else:
        print("Please enter h, l or c")
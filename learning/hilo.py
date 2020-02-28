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
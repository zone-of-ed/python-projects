"""
In this Python number guessing game, the computer selects a random number,
and the player tries to guess it. After each guess, the computer provides feedback,
telling the player whether the guess was too high, too low, or correct.
The game continues until the player guesses the correct number.

"""

# import random library
import random

guess_number = random.randint(1, 10) # Step 1

while True: # Step 2
    user_guess_number = int(input("Guess a number between 1 and 10: ")) # Step 3
    if user_guess_number == guess_number: # Step 4
        print("Congratulations! You guessed the number!")
        break
    elif user_guess_number < guess_number: # Step 5
        print("Your guess is too low!")
    elif user_guess_number > guess_number: # Step 6
        print("Your guess is too high!")
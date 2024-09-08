#!/usr/bin/python3

import random
import time

# Welcome message
welcome_message = """
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.

Please select the difficulty level:

    1. Easy (10 chances)
    2. Medium (5 chances)
    3. Hard (3 chances)
"""
print(welcome_message)

# Dictionary to store high scores for each difficulty level
high_scores = {
    "Easy": float('inf'),
    "Medium": float('inf'),
    "Hard": float('inf')
}


def provide_hint(my_guess):
    """
    Function to provide a hint to the user
    """
    hints = []
    if my_guess % 2 == 0:
        hints.append(f"The number is even.")
    else:
        hints.append(f"The number is odd.")

    divisors = [x for x in range(2, 11) if my_guess % x == 0]
    if divisors:
        hints.append(f"The number is divisible by {random.choice(divisors)}.")

    return random.choice(hints)


def number_guesser():
    """
    Main game logic
    """
    while True:
        try:
            # Get difficulty level from the user
            difficulty_level = int(input("Enter your choice (1 for Easy, 2\
 for Medium, 3 for Hard or 4 to quit): "))

            # Set the number of chances based on the difficulty level
            if difficulty_level == 1:
                mode = "Easy"
                chances = 10
            elif difficulty_level == 2:
                mode = "Medium"
                chances = 5
            elif difficulty_level == 3:
                mode = "Hard"
                chances = 3
            elif difficulty_level == 4:
                print("Okay then, come back anytime soon. Bye")
                exit()
            else:
                print("You have entered an incorrect mode, please try again.")
                continue

            print(f"\n\nGreat! You have selected the {mode} difficulty\
 level.\nLet's start the game!")
            my_guess = random.randint(1, 100)  # Generate randome number
            attempts = 0
            start_time = time.time()  # Start timer

            # User guessing loop
            while chances > 0:
                try:
                    user_guess = int(input("Enter your guess (between 1\
 and 100): "))
                    attempts += 1

                    if user_guess == my_guess:
                        end_time = time.time()  # End timer
                        total_time = round(end_time - start_time, 2)
                        print(f"Congratulations! You guessed the correct\
 number in {attempts} attempts and {total_time} seconds.")

                        # Check and update high score
                        if attempts < high_scores[mode]:
                            high_scores[mode] = attempts
                            print(f"New high score for {mode} difficulty:\
 {attempts} attempts!")
                        else:
                            print(f"Your high score for {mode} difficulty is\
 {high_scores[mode]} attempts.")

                        break
                    else:
                        chances -= 1
                        if user_guess < my_guess:
                            status = "greater"
                        else:
                            status = "less"
                        print(f"\nIncorrect! The number is {status} than\
 {user_guess}. You have {chances} chances left.")

                        # Provide a hint if the user is stuck
                        if chances == 2:
                            print("Hint: " + provide_hint(my_guess))

                        if chances == 0:
                            print(f"\nGame over! The number you failed to\
 guess was {my_guess}.")
                except ValueError:
                    print("Invalid input! Please enter a valid number between\
1 and 100.")
        except ValueError:
            print("Please enter a valid choice (1 for Easy, 2 for Medium, or 3\
 for Hard and 4 to quit the game).")


# initiate the call to the main function
number_guesser()

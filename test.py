#!/usr/bin/python3

import random

welcome_message = """
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.

Please select the difficulty level:

    1. Easy (10 chances)
    2. Medium (5 chances)
    3. Hard (3 chances)
                """

print(welcome_message)

try:
    difficulty_level = int(input("Enter your choice: "))

    if difficulty_level:
        mode = None
        chances = None

        if difficulty_level == 1:
            mode = "Easy"
            chances = 10
        elif difficulty_level == 2:
            mode = "Medium"
            chances = 5
        elif difficulty_level == 3:
            mode = "Hard"
            chances = 3
        else:
            print("You have entered the incorrect mode")
            exit()
    print("\n\nGreat! You have selected the {} difficulty level.\nLet's start\
 the game".format(mode))
    my_guess = random.randint(0, 100)
    print(my_guess)
    try:
        attempts = 0
        while chances > 0:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess == my_guess:
                print("Congratulations! You guessed the correct number in\
 {} attempts.".format(attempts))
                exit()
            else:
                chances -= 1
                if user_guess < my_guess:
                    status = "greater"
                elif user_guess > my_guess:
                    status = "less"
                print("Incorrect! The number is {} than {}.\
".format(status, user_guess))
                if chances == 0:
                    print("The number you failed to guess is {}\
".format(my_guess))
    except ValueError:
        print("Please guess a number between 0 and 100")

except ValueError:
    print("Please Enter either 1 for Easy, 2 for medium or 3 for Hard")
'''
try:
    selected_level = (int(input("Please select the difficulty level:\n1.\
 Easy(10 chances) \n2. Medium (5 chances)\n3. Hard (3 chances)\
 \n\nEnter you choice: ")))

except ValueError:
    print("Please enter either 1 for Easy, 2 for Meduim or 3 for Hard")

if level == 1:
    chances = 20
elif level == 2:
    chances = 10
elif level == 3:
    chances = 5

# generate a randome number between 0 and 100
number = random.randint(0, 100)

while chances > 0:

    # prompt user for number
    user_input = int(input("Please guess the number: "))

    # check wether user_input is the randome number
    if user_input == number:
        print("Your guess was right! .. you won!")
        exit(0)
    else:
        chances = chances - 1
        if user_input > number:
            print("{} is greater than the correct guess".format(user_input))
        elif user_input < number:
            print("{} is lesser than the correct guess".format(user_input))
        if chances == 0:
            print("The number you failed to guess is {}".format(number))
'''

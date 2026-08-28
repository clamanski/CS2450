# greet and welcome the user and let them know it is going to try and guess their age 
# Ask for name
# Guess age between 15-40 and respond with y or n
# If guess it correct is celebrates and says "<Your name> is <age> years old!"
# If guess is wrong it says "Rats" and tries to guess again until it gets the correct age

import random

def guess_age():
    print("Hello! Welcome to the Age Guesser Game!")
    name = input("What's your name? ")
    guess = random.randint(15, 40)
    while True:
        response = input(f"Is your age {guess}? (y/n): ").lower()
        if response == "y":
            print(f"Yay! {name} is {guess} years old!")
            break
        else:
            print("Rats!")
            guess = random.randint(15, 40)

if __name__ == "__main__":
    guess_age()


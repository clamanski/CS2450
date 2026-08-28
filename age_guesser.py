# greet and welcome the user and let them know it is going to try and guess their age 
# Ask for name
# Guess age between 15-40 and respond with y or n
# If guess it correct is celebrates and says "<Your name> is <age> years old!"
# If guess is wrong it says "Rats" and tries to guess again until it gets the correct age

import random

def guess_age():
    min_age = 15
    max_age = 40
    print("Hello! Welcome to the Age Guesser Game!")
    name = input("What's your name? ")
    guess = random.randint(min_age, max_age)
    while True:
        response = input(f"Is your age {guess}? (y/n): ").lower()
        if response == "y":
            print(f"Yay! {name} is {guess} years old!")
            break
        else:
            print("Rats!")
            print(min_age, max_age)
            hint = input("Are you older or younger than my guess? (o/y): ").lower()
            if hint == "o":
                if guess > min_age:
                    min_age = guess + 1
                    guess = random.randint(min_age, max_age)
            elif hint == "y":
                if guess < max_age:
                    max_age = guess - 1
                    guess = random.randint(min_age, max_age)

            
if __name__ == "__main__":
    guess_age()



'''
Pseudocode

Import random to use it
Declare the variables rock paper and scissors to use ascii art
Make a list for the choices (Rock, paper, scissors)
Ask the user for their input and store it
Make the computer pick a random choice from our list and store it
Write a if statement for input validation in case the user inputs something wrong
Write if statements for each outcome
Write else statement at the end to print in case of wrong user input

'''

import random

# Variable for rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Variable for paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Variable for scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

RPS = [rock, paper, scissors]  # Making the variables above into a list

# Prompting the user to make their choice
userChoice = input('Welcome to Rock Paper Scissors.\n'
                   # Using .lower to ensure right response
                   'Please pick between rock, paper, or scissors: ').lower()

# Making the computer to pick at random
computerChoice = random.choice(RPS)

# Input validation in case user input is wrong
if userChoice == "rock" or userChoice == "paper" or userChoice == "scissors":

    if userChoice == "rock":  # If the user picks rock
        print("Your choice:\n")
        print(rock)

        print("Computers choice:\n")
        print(computerChoice)

        if computerChoice == rock:
            print("Draw!")

        elif computerChoice == paper:
            print("You lose!")

        else:
            print("You win!")

    elif userChoice == "paper":  # If user picks paper
        print("Your choice:\n")
        print(paper)

        print("Computers choice:\n")
        print(computerChoice)

        if computerChoice == paper:
            print("Draw!")

        elif computerChoice == scissors:
            print("You lose!")

        else:
            print("You win!")

    else:  # If user picks scissors
        print("Your choice:\n")
        print(scissors)

        print("Computers choice:\n")
        print(computerChoice)

        if computerChoice == scissors:
            print("Draw!")

        elif computerChoice == rock:
            print("You lose!")

        else:
            print("You win!")

else:
    print("You picked an incorrect choice, please rerun program and try again.")

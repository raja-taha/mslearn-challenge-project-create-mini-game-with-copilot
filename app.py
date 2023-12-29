# make a rock paper scissors game with pc as a multiplayer

import random

print("Welcome to Rock, Paper, Scissors game!")
user = input("Choose your weapon: ")
user = user.lower()
while user != "rock" and user != "paper" and user != "scissors":
    print("Invalid Input!")
    user = input("Choose your weapon: ")
    user = user.lower()
print("Your weapon is: " + user)
computer = random.choice(["rock", "paper", "scissors"])
print("Computer's weapon is: " + computer)
if user == computer:
    print("It's a tie!")
elif user == "rock":
    if computer == "paper":
        print("You lose!")
    else:
        print("You win!")
elif user == "paper":
    if computer == "scissors":
        print("You lose!")
    else:
        print("You win!")
elif user == "scissors":
    if computer == "rock":
        print("You lose!")
    else:
        print("You win!")

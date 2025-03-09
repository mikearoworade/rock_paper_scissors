# ROCK, PAPER and SCISSORS
from art import logo, symbol, option
from random import randint

print(logo)
print("Welcome to Rock Paper Scissors!")
name = input("What is your name? ")
print(f"Hi {name}!\nThe rules of the game is as follow:\n Rock wins scissors\n Paper wins rock\n "
      f"Scissors win paper.\n")

play_again = True
while play_again:
    user_choice = int(input(f"{name}, Now type 0 for Rock, 1 for Paper, 2 for Scissors: "))

    if user_choice >= 3 or user_choice < 0:
        print(f"Invalid input {name}")
    else:
        print(f"{name} chose {option[user_choice]} {symbol[user_choice]}")
        computer_choice = randint(0, 2)
        print(f"Computer chose {option[computer_choice]} {symbol[computer_choice]}")
        if user_choice == computer_choice:
            print("It's a tie!")
        elif user_choice == 0 and computer_choice == 1:
            print(f"{name} you lose 😓")
        elif user_choice == 0 and computer_choice == 2:
            print(f"{name} you win 🏆")
        elif user_choice == 1 and computer_choice == 0:
            print(f"{name} you win 🏆")
        elif user_choice == 1 and computer_choice == 2:
            print(f"{name} you lose 😓")
        elif user_choice == 2 and computer_choice == 0:
            print(f"{name} you lose 😓")
        elif user_choice == 2 and computer_choice == 1:
            print(f"{name} you win 🏆")

    answer = input("Will you love to play again? Type y for yes OR n for no: ").lower()
    if answer != 'y':
        play_again = False
        print("Thank you for playing!")

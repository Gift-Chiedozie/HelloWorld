import random

rock = """

"""
paper = """

"""
scissors = """

"""

game_images = [rock, paper, scissors]
user_choice = int(input("Enter your choice: 0 for Rock, 1 for Paper, 2 for Scissors\n> "))
if user_choice >= 3 or user_choice < 0:
    print("You have entered an invalid input, You Lose!")
else:
    print(game_images[user_choice])
    computer_choice = random.randint(0,2)
    print("Computer chose: ")
    print(game_images[computer_choice])
    if computer_choice == user_choice:
        print("It's a draw!")
    elif computer_choice == 0 and user_choice == 2:
        print("Computer wins!")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice > user_choice:
        print("Computer wins!")
    elif user_choice > computer_choice:
        print("You win!")
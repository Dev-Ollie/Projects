#Made by Ollie'5248 on Discord :)
import time
import random
from random import randint

wait_time = 3 # Feel free to change this value, this is how long the program waits in seconds before executing the next stage of the program. :)

play_options = ["Rock", "Paper", "Scissors"]



player = False

while player == False:
    print("Welcome to Rock, Paper, Scissors in Python!\n\nPlease enter any of the following 'Rock', 'Paper' or 'Scissors'\n\nThe game will begin with Rock, Paper, Scissors, Shoot...")
    time.sleep(wait_time)
    player_option = input("\nRock, \nPaper, \nScissors, \nShoot...\n\nPlease enter your decision: ")
    computer_move = play_options[randint(0, 2)]
    if player_option in play_options:
        time.sleep(wait_time)
        if player_option == "Rock":
            if computer_move == "Rock":
                print("\nTie, you both picked Rock!")
            elif computer_move == "Scissors":
                print("\nYou won, Rock beats Scissors!")
            elif computer_move == "Paper":
                print("\nYou lost, Paper covers Rock!")

        elif player_option == "Paper":
            if computer_move == "Paper":
                print("\nTie, you both picked Paper!")
            elif computer_move == "Scissors":
                print("\nYou lost, Scissors cuts Paper!")
            elif computer_move == "Rock":
                print("\nYou won, Paper covers Rock!")

        elif player_option == "Scissors":
            if computer_move == "Paper":
                print("\nYou won, Scissors cuts Paper!")
            elif computer_move == "Rock":
                print("\nYou lost, Rock beats Scissors!")
            elif computer_move == "Scissors":
                print("\nTie, you both picked Scissors!")
        time.sleep(wait_time)
        print("\n----------\n")
        player = False
    else:
        print("\nPlease enter a valid move to play.")
        print("\n----------\n")
        time.sleep(wait_time)
        player = False
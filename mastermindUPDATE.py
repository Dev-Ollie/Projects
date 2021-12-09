import time
import random

max_goes = 16
colours = ["blue", "black", "green", "red", "white", "yellow"]
colours_correct = 0
correct = 0
attempt = 0
wait_time = 4

def resetStats():
    global correct
    global colours_correct
    correct = 0
    colours_correct = 0

x = False
while x == False:
    x = True
    print("Welcome to MasterMind on Python vs. The Computer")
    time.sleep(wait_time)
    print("\nThe Computer will select 4 colours, either blue, black, green, red, white or yellow.\n\nIt is your job to guess in the correct order the colours that the computer has thought of.\n\nYou have 16 goes, good luck!")
    time.sleep(wait_time)
    print("\nYou will be awarded a black pin for each colour guessed correctly and it is in the correct order.\n\nYou will be awarded a white pin for each colour guessed correctly but in the wrong place.")
    time.sleep(wait_time)
    start = input("\nAre you ready to start the game?\n\nPlease enter 'y' to begin: ")
    time.sleep(wait_time)
    if start == 'y':
        print("\nStarting the game, good luck...")
        time.sleep(wait_time)
        computer_selection = random.sample(colours, 4)
        time.sleep(wait_time) 
        print("\nThe Computer has selected it's Colours!")
        print(computer_selection)
        
        while attempt < max_goes:
            attempt += 1
            colour_selection = input("\nPlease enter your choice of colours: ")
            def convert(colour_selection):
                return (colour_selection.split())
            colour_input_table = convert(colour_selection)
            for i in colour_input_table:
                for k in colours:
                    if i == k:
                        resetStats()

            for i in computer_selection:
                for k in colour_input_table:
                    if i == k:
                        if computer_selection.index(i) == colour_input_table.index(k):
                            correct += 1
                        else:
                            colours_correct += 1
            if correct > 0:
                if correct == 1:
                    print("\nYou got", correct, "black pin.")
                else:
                    print("\nYou got", correct, "black pins.")

            if colours_correct > 0:
                if colours_correct == 1:
                    print("\nYou got", colours_correct, "white pin.")
                else:
                    print("\nYou got", colours_correct, "white pins.")

            if correct == 4:
                print("\nWell done, you win!")
                print("\n----------\n")
                time.sleep(wait_time)
                x = False
                time.sleep(wait_time)
                break
            goes_left = max_goes - attempt
            print("\nYou have", goes_left, "more attempts.")
            if goes_left == 0:
                print("\nThe correct answer was: {} {} {} {}" .format(computer_selection[0], computer_selection[1], computer_selection[2], computer_selection[3]))
                print("\n----------\n")
                time.sleep(wait_time)
                x = False
    else:
        print("\nEnter 'y' to play the game!\n")
        print("---------\n")
        time.sleep(wait_time)
        x = False
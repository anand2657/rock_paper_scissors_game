import sys
import os

# Explicitly add current directory to Python search path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from config import OPTIONS

def get_number_of_rounds():
    """Prompts for total rounds and handles invalid text inputs."""
    while True:
        try:
            rounds = int(input("Select the number of rounds to play: "))
            if rounds > 0:
                return rounds
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input! Please enter a whole number.")

def get_user_choice():
    """Gets and validates user move."""
    while True:
        move = input("\nEnter rock, paper or scissors: ").lower().strip()
        if move in OPTIONS:
            return move
        print("Invalid input, please type rock, paper or scissors.")
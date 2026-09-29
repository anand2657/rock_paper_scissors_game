import random
from config import OPTIONS

def get_computer_choice():
    """Generates computer's move."""
    choice = random.choice(OPTIONS)
    print(f"Computer chose: {choice}")
    return choice
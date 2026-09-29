from config import WINNING_PAIRS

def determine_round_winner(user_move, computer_move):
    """Evaluates the winner for a single round."""
    if user_move == computer_move:
        print("Tie!")
        return "tie"
    elif WINNING_PAIRS[user_move] == computer_move:
        print("You win!")
        return "user"
    else:
        print("Computer wins!")
        return "computer"

def display_summary(user_points, computer_points):
    """Prints final score summary."""
    print("\n--- Game Over ---")
    print(f"Final Score -> You: {user_points} | Computer: {computer_points}")
    if user_points > computer_points:
        print("Congratulations! You won the match!")
    elif user_points < computer_points:
        print("Computer won the match!")
    else:
        print("The match ended in a tie!")
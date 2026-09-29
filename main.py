
from user_input import get_number_of_rounds, get_user_choice
from computr import get_computer_choice
from game_logic import determine_round_winner, display_summary


def main():
    player_score = 0
    machine_score = 0
    rounds_played = 0

    rounds_to_play = get_number_of_rounds()

    while rounds_played < rounds_to_play:
        player_pick = get_user_choice()
        machine_pick = get_computer_choice()

        round_outcome = determine_round_winner(player_pick, machine_pick)

        if round_outcome == "user":
            player_score += 1
        elif round_outcome == "computer":
            machine_score += 1

        rounds_played += 1
        print(f"Score - You: {player_score} | Computer: {machine_score}")

    display_summary(player_score, machine_score)


if __name__ == "__main__":
    main()

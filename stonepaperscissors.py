# ==========================================
# IMPORTING NECESSARY MODULES
# ==========================================
# We import 'random' so the computer can make a random choice later.
import random


# ==========================================
# HELPER FUNCTIONS (The Building Blocks)
# ==========================================
def calculate_win_percentage(wins, total_rounds):
    """Calculates what percentage of rounds the player won."""
    # Safety Check: If they played 0 rounds, we can't divide by 0 (it crashes the program).
    if total_rounds == 0:
        return 0.0

    # Math formula: (Wins divided by Total Rounds) multiplied by 100
    percentage = (wins / total_rounds) * 100

    # round(..., 1) cuts the decimal down to just 1 digit (e.g., 66.66% becomes 66.7%)
    return round(percentage, 1)


def get_computer_choice():
    """Makes a random selection for the computer."""
    # List of all valid options
    options = ["stone", "paper", "scissors"]

    # random.choice picks one item out of the list completely at random
    computer_pick = random.choice(options)
    return computer_pick


def determine_winner(player, computer):
    """Compares choices and returns 'win', 'lose', or 'tie'."""
    # Step 1: Check if it's a tie
    if player == computer:
        return "tie"

    # Step 2: Check all 3 specific rules where the PLAYER wins:
    # - Stone beats Scissors
    # - Paper beats Stone
    # - Scissors beats Paper
    if player == "stone" and computer == "scissors":
        return "win"
    elif player == "paper" and computer == "stone":
        return "win"
    elif player == "scissors" and computer == "paper":
        return "win"

    # Step 3: If it's not a tie and the player didn't win, the computer must have won.
    else:
        return "lose"


# ==========================================
# MAIN GAME FUNCTION (Where everything runs)
# ==========================================
def play_game():
    print("=========================================")
    print("  WELCOME TO STONE, PAPER, SCISSORS!     ")
    print("=========================================\n")

    # Ask the player for their name
    player_name = input("Enter your name: ").strip()

    # If the user just presses Enter without typing, give them a default name
    if player_name == "":
        player_name = "Player"

    # OUTER LOOP: Keeps the entire game application running
    while True:
        # Ask the user to choose a game mode
        print("\nChoose Game Mode:")
        print("1. Endless Mode (Play as long as you want)")
        print("2. Best of 3 (First to 2 wins)")
        print("3. Best of 5 (First to 3 wins)")
        mode_choice = input("Enter your choice (1/2/3): ").strip()

        # Set up rules for the chosen mode
        target_wins = 0  # Default is 0 for Endless mode

        if mode_choice == "2":
            target_wins = 2  # First to 2 wins
            print("\n--- Match Mode: Best of 3 Activated! ---")
        elif mode_choice == "3":
            target_wins = 3  # First to 3 wins
            print("\n--- Match Mode: Best of 5 Activated! ---")
        else:
            print("\n--- Match Mode: Endless Activated! ---")

        # Score Tracker Variables (all start at 0)
        
        player_score = 0
        computer_score = 0
        total_rounds = 0

        # INNER LOOP: Handles the individual rounds inside a single match
        while True:
            # Display current round number (Starts at 1 because total_rounds is 0)
            print(f"\n--- Round {total_rounds + 1} ---")

            # Get user choice, remove extra spaces (.strip), make it lowercase (.lower)
            player_choice = (
                input("Choose Stone, Paper, or Scissors: ").strip().lower()
            )

            # Check if what the user typed is actually valid
            if player_choice not in ["stone", "paper", "scissors"]:
                print(
                    " Typo or invalid choice! Please type Stone, Paper, or Scissors."
                )
                continue  # 'continue' skips everything below and restarts this round loop

            # Get the computer's random choice
            computer_choice = get_computer_choice()
            print(f" Computer chose: {computer_choice.capitalize()}")

            # Compare choices to see who won this round
            round_result = determine_winner(player_choice, computer_choice)

            # Update scores based on the result
            if round_result == "tie":
                print(" It's a Draw/Tie!")
            elif round_result == "win":
                print(f" {player_name} wins this round!")
                player_score = player_score + 1  # Add 1 point to player
            else:
                print(" Computer wins this round!")
                computer_score = computer_score + 1  # Add 1 point to computer

            # Add 1 to total rounds played
            total_rounds = total_rounds + 1

            # Print the live score update
            print(
                f" Scores -> {player_name}: {player_score} | Computer: {computer_score}"
            )

            # Check if someone won in 'Best of 3' or 'Best of 5' modes
            if target_wins > 0:
                if player_score == target_wins:
                    print(
                        f"\n CONGRATULATIONS {player_name.upper()}! You won the entire match! 🏆"
                    )
                    break  # 'break' stops the round loop because the match is over

                elif computer_score == target_wins:
                    print(
                        "\n Computer won the entire match! Better luck next time! 🤖"
                    )
                    break  # 'break' stops the round loop because the match is over

            # If playing Endless Mode, ask if they want to stop after this round
            if target_wins == 0:
                keep_playing = (
                    input("Do you want to play another round? (y/n): ")
                    .strip()
                    .lower()
                )
                if keep_playing == "n":
                    break  # 'break' stops the endless round loop

        # ==========================================
        # MATCH IS OVER: SHOW FINAL STATISTICS
        # ==========================================
        # Calculate the win rate using our helper function
        win_rate = calculate_win_percentage(player_score, total_rounds)

        # Calculate how many draws happened
        draws = total_rounds - (player_score + computer_score)

        print("\n=========================================")
        print("               FINAL SCORE               ")
        print("=========================================")
        print(f" Player Name:    {player_name}")
        print(f" Total Rounds:   {total_rounds}")
        print(f" Your Wins:      {player_score}")
        print(f" Computer Wins:  {computer_score}")
        print(f" Total Draws:    {draws}")
        print(f" Win Percentage: {win_rate}%")
        print("=========================================\n")

        # ==========================================
        # BONUS FEATURE: PLAY AGAIN OPTION
        # ==========================================
        # Ask if they want to boot up a whole new game session
        play_again_choice = (
            input("Do you want to start a brand new match? (yes/no): ")
            .strip()
            .lower()
        )

        # If they type anything other than 'yes' or 'y', close the game
        if play_again_choice not in ["yes", "y"]:
            print(f"\nThanks for playing, {player_name}! Goodbye! ")
            break  # 'break' exits the outer loop, which ends the program


# This line makes sure the game runs immediately when you launch the file
if __name__ == "__main__":
    play_game()
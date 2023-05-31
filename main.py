import random


# Define functions
# Get the player's choice of rock, paper, or scissors.
def get_player_option(valid_choices):
    while True:
        choice = input("Make your choice: ").lower()
        if choice in valid_choices:
            return choice
        print("Invalid choice, please try again.")


# Determine the winner of a round based on the players' choice
def make_rules(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
            (player_choice == "paper" and computer_choice == "rock") or \
            (player_choice == "scissors" and computer_choice == "paper"):
        return "player"
    else:
        return "computer"


# Print the current score.
def print_score(player_score, computer_score):
    print(f"\nCurrent score: You {player_score}, Computer {computer_score}")


def the_game():
    valid_choices = ("rock", "paper", "scissors")
    print("Welcome to the amazing game of Rock paper scissors:")
    num_rounds = int(input("\nHow many rounds do you want to play? "))
    player_score = 0
    computer_score = 0

    for i in range(1, num_rounds + 1):
        print(f"\nRound {i}:")

        # Get player and computer choices
        player_choice = get_player_option(valid_choices)
        computer_choice = random.choice(valid_choices)

        # Print computer's choice
        print("\nThe computer choice:", computer_choice)

        # Determine winner of round
        result = make_rules(player_choice, computer_choice)
        if result == "player":
            player_score += 1
            print("You win this round!")
        elif result == "computer":
            computer_score += 1
            print("\nSorry, you lost this round.")
        else:
            print("It's a tie!")

        # Print current score
        print_score(player_score, computer_score)

    # Check if someone has won the game
    if player_score > computer_score:
        print("\nWohoo! You win the game!")
    elif computer_score < computer_score:
        print("\nSorry, you lost the game!")
    else:
        print("It's a tie game!")


# Call the game
the_game()

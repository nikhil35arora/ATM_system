import random


VALID_CHOICES = ("stone", "paper", "scissors")


def get_computer_choice():
    return random.choice(VALID_CHOICES)


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"

    winning_moves = {
        "stone": "scissors",
        "paper": "stone",
        "scissors": "paper",
    }

    if winning_moves[user_choice] == computer_choice:
        return "user"
    return "computer"


def play_round():
    user_choice = input("Enter stone, paper, or scissors: ").strip().lower()
    if user_choice not in VALID_CHOICES:
        print("Invalid choice. Please enter stone, paper, or scissors.")
        return

    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if result == "draw":
        print("Result: It's a draw!")
    elif result == "user":
        print("Result: You win!")
    else:
        print("Result: Computer wins!")


def run_game():
    while True:
        print("\n--- Stone Paper Scissors ---")
        print("1. Play a round")
        print("2. Exit")

        option = input("Choose an option (1-2): ").strip()

        if option == "1":
            play_round()
        elif option == "2":
            print("Thanks for playing!")
            break
        else:
            print("Invalid option. Please choose 1 or 2.")


if __name__ == "__main__":
    run_game()

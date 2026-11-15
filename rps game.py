import random

def main():
    print("--- ROCK PAPER SCISSORS GAME ---")

    user_score = 0
    computer_score = 0

    choices = ["rock", "paper", "scissors"]

    while True:
        print("\nChoose one:")
        print("Rock")
        print("Paper")
        print("Scissors")

        user_choice = input("Enter your choice: ").strip().lower()

        if user_choice not in choices:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            continue

        #Generate computer choice
        computer_choice = random.choice(choices)

        print(f"\nYour Choice: {user_choice.capitalize()}")
        print(f"Computer Choice: {computer_choice.capitalize()}")

        #Determine winner
        if user_choice == computer_choice:
            print("It's a tie!")

        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            print("You win!")
            user_score += 1

        else:
            print("Computer wins!")
            computer_score += 1

        #Display scores
        print("\nScore Board")
        print(f"User: {user_score}")
        print(f"Computer: {computer_score}")

        #Play again
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()

        if play_again != "yes":
            print("\nFinal Score")
            print(f"User: {user_score}")
            print(f"Computer: {computer_score}")
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()
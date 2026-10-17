import random

computer_choices = ["rock", "paper", "scissors"]

while True:

    print("1. Play Game")
    print("2. Exit")

    choice = input("Enter the number: ")

    if choice == "1":

        my_choice = input("Enter your choice: ").lower()

        comp_choice = random.choice(computer_choices)

        print("Computer choice:", comp_choice)

        if my_choice == comp_choice:
            print("Tie")

        elif my_choice == "rock" and comp_choice == "scissors":
            print("You win")

        elif my_choice == "scissors" and comp_choice == "paper":
            print("You win")

        elif my_choice == "paper" and comp_choice == "rock":
            print("You win")

        elif my_choice == "rock" and comp_choice == "paper":
            print("You lose")

        elif my_choice == "scissors" and comp_choice == "rock":
            print("You lose")

        elif my_choice == "paper" and comp_choice == "scissors":
            print("You lose")

        else:
            print("Invalid choice!")

    elif choice == "2":
        print("Game exited.")
        break

    else:
        print("Invalid choice!")
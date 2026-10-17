import random

my_choice = input("Enter your choice: ").lower()

computer_choices = ["rock", "paper", "scissors"]

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
    print("Invalid choice! Please enter rock, paper, or scissors.")
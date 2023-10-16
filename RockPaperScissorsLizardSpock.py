import random

rpsls = ("rock", "paper", "scissors", "lizard", "spock")
active = True

while active:
   
    computer = random.choice(rpsls)
    player = input("What would you like to pick? Rock, Paper, Scissors, Lizard, or Spock  ").lower()
    print(f"Player picked {player}")
    print(f"Computer picked {computer}")

    if player == computer:
        print("It's a Tie")
    elif (player == "rock" or player == "spock") and computer == "scissors":
        print("You Win!")
    elif (player == "scissors" or player == "lizard") and computer == "paper":
        print("You Win!")
    elif (player == "paper" or player == "spock") and computer == "rock":
        print("You Win!")
    elif (player == "scissors" or player =="rock") and computer == "lizard":
        print("You Win!")
    elif (player == "lizard" or player == "paper") and computer == "spock":
        print("You Win!")
    else:
        print("You Lose!")
    if not input("Play again? (y/n): ").lower() == "y":
        active = False

print("Thank God this finally worked!")
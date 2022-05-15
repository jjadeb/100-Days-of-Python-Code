import random

## Roxk paper scissors art from <script src="https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe.js"></script>

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print("Welcome to the game Rock, Paper, Scissors! Good luck!")
rps = input("What do you choose? Rock, Paper, or Scissors \n").lower()

if rps == "rock":
  print("Your choice:")
  print(rock)
elif rps == "paper":
  print("Your choice:")
  print(paper)
elif rps == "scissors":
  print("Your choice:")
  print(scissors)
else:
  print("That is not a valid choice.")
  quit()

rock_paper_scissors = ["rock", "paper", "scissors"]
computer_choice = random.choice(rock_paper_scissors)

if computer_choice == "rock":
  print("Computer's choice:")
  print(rock)
elif computer_choice == "paper":
  print("Computer's choice:")
  print(paper)
else:
  print("Computer's choice:")
  print(scissors)

if computer_choice == rps:
  print("There is a tie.")
elif (rps == "rock" and computer_choice == "scissors") or (rps == "scissors" and computer_choice == "paper") or (rps == "paper" and computer_choice == "rock"):
  print("You win!")
else:
  print("You lose")




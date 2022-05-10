#Number Guessing Game Objectives:

#Imports
import art
import random
import os

#Game Code
def number_guess_game():
  #Print Welcome
  print(art.logo)
  print("Welcome to Guess the Number!! A random number has been chosen between 1 and 100.")
  
  #Choose random #
  number = random.randint(1,100)
  
  #Set difficulty level
  difficulty = input("What difficulty level would you like? Type 'easy' for 10 guesses, or 'hard' for 5 guesses:\n ")
  guesses = 0
  if difficulty == "easy":
    guesses = 10
  elif difficulty == "hard":
    guesses = 5
  else:
    print("That is not a valid guess.")
    exit()
  
  #Guessing Time
  won = False
  while not won and guesses > 0:
    guess = int(input("What is your guess: "))
    if guess > number:
      print("Too high!")
      guesses -= 1
    elif guess < number:
      print("Too low!")
      guesses -= 1
    else:
      return True
  return False

#Play again? and win/lose output
play_again = True
while play_again == True:
  os.system('clear')
  if number_guess_game():
    print("You guessed correctly! You win!")
  else:
    print("You ran out of guesses. You lose.")
  y_n = input("Would you like to play again? Type 'y' for yes or 'n' for no.")
  if y_n == 'n':
    play_again = False

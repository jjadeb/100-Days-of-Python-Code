# All code written myself

#Import Statements
import art
import random
import game_data
import os


#Randonly pick first person
length_data = len(game_data.data)
first_num = random.randrange(length_data)

points = 0
already_done = []

def pick_second(num1):
  '''Pick the second person to be compared'''
  num2 = random.randrange(length_data)
  while num1 == num2 or num2 in already_done:
    num2 = random.randrange(length_data)
  already_done.append(num2)
  return num2

def higher_lower(num1): 
  #Print Header graphic
  print(art.logo)

  global points
  print(f"You have {points} point(s).")

  
 #Randomly pick 2nd person
  num2 = pick_second(num1)

  #Find person in list of game data
  person1 = game_data.data[num1]
  person2 = game_data.data[num2]

  #Print first persons info
  name1 = person1.get('name')
  follower_count1 = person1.get('follower_count')
  description1 = person1.get('description')
  country1 = person1.get('country')

  print(f"Compare A: {name1}, a {description1}, from {country1}.")

  #Print 'VS' symbol
  print(art.vs)

  #Print second persons info
  name2 = person2.get('name')
  follower_count2 = person2.get('follower_count')
  description2 = person2.get('description')
  country2 = person2.get('country')

  print(f"Compare B: {name2}, a {description2}, from {country2}.")

  #Find corrct choice
  correct_answer = "c"
  correct_person = {}
  if follower_count1 > follower_count2:
    correct_answer = "a"
    correct_person = num1
  elif follower_count1 < follower_count2: 
    correct_answer = "b"
    correct_person = num2

  #Ask for their choice
  choice = input("Who has more followers, A or B? \n").lower()

  #Is choice correct?
  if choice == correct_answer:
    points += 1
    os.system('clear')
    if points == length_data - 1:
      print("You win! No more people left!")
      return
    higher_lower(correct_person)
  else:
    os.system('clear')
    print(f"You lose. Final score: {points}")

higher_lower(first_num)
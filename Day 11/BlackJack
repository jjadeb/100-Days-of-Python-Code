############### Blackjack Project #####################


## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
import os

# List of cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



def blackjack():

  ### ASSIGNING VARIABLES
  
  #Setting up computers cards
  computer_cards = []
  comp_card1 = random.choice(cards)
  comp_card2 = random.choice(cards)
  computer_cards.append(comp_card1)
  computer_cards.append(comp_card2)
  
  
  #Setting up users cards
  users_cards = []
  users_card1 = random.choice(cards)
  users_card2 = random.choice(cards)
  users_cards.append(users_card1)
  users_cards.append(users_card2)
  users_total = 0

  ### DEFINITIONS

  #End of Game
  def end_game():
  
    def user_lose(reason):
      print(f"{reason} You lose!😞")
  
    def user_win(reason):
      print(f"{reason} You win!😁")
    
    #Counting up totals
    user_total = 0
    computer_total = 0
    for card in users_cards:
      user_total += card
    for card in computer_cards:
      computer_total += card
  
    #Printing information
    print(f"Your final hand: {users_cards}, final score: {users_total}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_total}")
  
    #Printing Outcome
    if users_total > 21:
      user_lose("Busted!")
    elif computer_total > 21:
      user_win("Computer busted!")
    elif computer_total == 21:
      user_lose("Computer got a blackjack.")
    elif user_total == 21:
      user_win("You got a blackjack!")
    elif user_total > computer_total:
      user_win("You got more than the computer!")
    else:
      user_lose("You got less or equal to the computer.")
    again = input("Do you want to play again? Type 'y' or 'n': ")
    if again == 'y': 
      os.system('clear')
      blackjack()
    else:
      os.system('clear')
  
  
  #Printing information
  def print_user_info():
    print(f"users cards: {users_cards}, current score: {users_total}")
    
  
  #Computer draws card
  def comp_draw_card():
    '''Draws another card for the computer'''
    comp_card = random.choice(cards)
    return comp_card
  
  #User draws card
  def user_draw_card():
    '''Draws another card for the user'''
    users_card = random.choice(cards)
    return users_card
  
  #Computer draws cards until bust or higher than user
  def comp_draw_until_done():
    '''Draw cards for computer until value is not less than users value'''
    computer_total = comp_total
    while computer_total < users_total and computer_total <= 21:
      card = comp_draw_card()
      computer_total += card
      computer_cards.append(card)
      if computer_total > 21 and 11 in computer_cards:
        computer_cards.remove(11)
        computer_cards.append(1)
        computer_total -= 10
  
  #### GAME CODE
  print("Welcome to Blackjack!")
        
  users_total = users_card1 + users_card2
  comp_total = comp_card1 + comp_card2

  print_user_info()
  print(f"Computer's first card: {comp_card1}")
  
  if users_total == 21:
    comp_draw_until_done()
    end_game()
    return

    
  #Asking if the user wants to hit or pass
  cont = input("Type 'h' to hit, type 'p' to pass: ")
  while cont == 'h':
    new_val = user_draw_card()
    users_cards.append(new_val)
    users_total += new_val
    if users_total > 21 and 11 in users_cards:
        users_cards.remove(11)
        users_cards.append(1)
        users_total -= 10
    if users_total >= 21:
      comp_draw_until_done()
      end_game()
      return
    print_user_info()
    cont = input("Type 'h' to hit, type 'p' to pass: ")
  comp_draw_until_done()
  end_game()



blackjack()
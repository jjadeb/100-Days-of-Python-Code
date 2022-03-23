

def main() :
  print("Welcome to the tip calculator!")
  
  cost = float(input("What was the total bill?\n"))
  tip = int(input("How much tip would you like to give?    10, 12, or 15?\n"))
  num_people = int(input("How many people to split the bill?\n"))
  
  total_cost = cost * (1 + tip * 0.01)
  cost_per_person = total_cost / num_people
  final_cost = "{:.2f}".format(cost_per_person)
  
  print(f"Each person should pay: ${final_cost}")



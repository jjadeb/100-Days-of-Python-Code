

def main() :
  print("Welcome to the tip calculator!");
  
  bill = float(input("What was the total bill?\n"));
  tip = int(input("How much tip would you like to give?    10, 12, or 15?\n"));
  people = int(input("How many people to split the bill?   \n"));
  
  total_bill = bill * (1 + tip * 0.01);
  bill_per_person = total_bill / people;
  final_cost = "{0.2f}".format(bill_per_person);
  
  print(f"Each person should pay: ${final_cost}");



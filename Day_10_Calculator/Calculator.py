
#Add
def add(a, b):
  return a + b

#Subtract
def sub(a, b):
  return a-b

#Multiply
def multiply(a, b):
  return a*b

#Devide
def devide(a, b):
  return a/b

operations = {
  "+": add,
  "-": sub,
  "*": multiply,
  "/": devide,
}


def calculator():
  num1 = float(input("What is the first number: "))
  
  cont = "yes"
  while cont == "yes":  
    op = input("What operation would you like to use? Type +, -, *, / ")
    num2 = float(input("What is the second number: "))
    
    answer = operations[op](num1, num2)
    print(f"{num1} {op} {num2} = {answer}.")
    num1 = answer
    cont = input("Would you like to continue calculating using this number? Type yes to continue or no to start fresh with new numbers: ")
  calculator()

calculator()

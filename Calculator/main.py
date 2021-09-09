from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2


operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}


def calculator():
  
  print(logo)
  num1 = float(input("What is the first number?: "))


  for symbol in operations:
    print(symbol)

  progress = True

  while(progress):

    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What is the next number?: "))

    for symbol in operations:
      if operation_symbol == symbol:
        answer = operations[symbol](num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    index = input(f"Type 'y' to continue calculating with {answer},  or 'n' to " +
            "start a new calculation, if you want to exit, type 'exit': ")
    if index == 'y':
      num1 = answer
    elif index == 'no':
      progress = False
      calculator()
    else:
        break

calculator()

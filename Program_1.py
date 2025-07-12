class Calculator:
  def __init__(self):
    pass
  def add(self, a, b):
    return a + b
  def subtract(self, a, b):
    return a - b
  def multiply(self, a, b):
    return a * b
  def divide(self, a, b):
    if b == 0:
      return "Error:Cannont divide by zero"
    return a / b
try:
  num1=float(input("Enter first number(a): "))
  num2=float(input("Enter second number(b): "))
  operation=input("Enter the type of operation(Addition,Subtraction,Multiplication,Division):").lower()
  calculator=Calculator()
  if operation=="addition":
    result=calculator.add(num1,num2)
  elif operation=="subtraction":
    result=calculator.subtract(num1,num2)
  elif operation=="multiplication":
    result=calculator.multiply(num1,num2)
  elif operation=="division":
    result=calculator.divide(num1,num2)
  else:
    print("Invalid operation")
    result="Error:Invalid operation"
  print("Result:",result)
except ValueError:
  print("Invalid input.Please enter valid numbers.")

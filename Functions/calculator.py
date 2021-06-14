# Function for addition
def add(num1, num2):
    return num1 + num2
  
# Function for subtraction
def subtract(number1, number2):
    return number1 - number2
  
# Function for multiplying
def multiply(number1, number2):
    return number1 * number2
  
# Function for dividing
def divide(number1, number2):
    return number1 / number2
  
print("Operations calculator can perform:")
print("Add")
print("Subtract")
print("Multiply")
print("Divide")
  
  
# Take input from the user 
select = input("Select operations form:")
  
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
  
if select == 'add':
    print(number_1, "+", number_2, "=",
                    add(number_1, number_2))
  
elif select == 'Subtract':
    print(number_1, "-", number_2, "=",
                    subtract(number_1, number_2))
  
elif select == 'Multiply':
    print(number_1, "*", number_2, "=",
                    multiply(number_1, number_2))
  
elif select == 'Divide':
    print(number_1, "/", number_2, "=",
                    divide(number_1, number_2))
else:
    print("Invalid operation")
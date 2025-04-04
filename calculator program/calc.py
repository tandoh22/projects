# this is a simple python calculator program
operator = input("enter an operator: ")
num1 = float(input('enter the first number: '))
num2 = float(input('enter the second number: '))

if operator == '+':
    result = num1 + num2
    print(result)
elif operator == '-':
    result = num1 - num2
    print(result)    
elif operator == '*':
    result = num1 * num2
    print(result)    
elif operator == '/':
    result = num1 / num2
    print(result)      
else:
    print(f"{operator} is invalid, try again")    
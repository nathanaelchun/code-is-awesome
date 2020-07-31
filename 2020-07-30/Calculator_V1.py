number1 = input("Enter a random number:")
operation = input("Enter a operation:")
number2 = input("Enter a random number:")
number1a = int(number1)
number2a = int(number2)
if operation == "+":
    answer = number1a+number2a
elif operation == "-":
    answer = number1a-number2a
elif operation == "*":
    answer = number1a*number2a
elif operation == "/":
    answer = number1a/number2a

print(number1,operation,number2,"=",answer)
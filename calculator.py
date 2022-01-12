print("This is the calculator project")

number1 = int(input("What is your first number?"))
number2 = int(input("What is your second number?"))

operator = input("Do you want to add, multiply, subtract or divide")

if operator == "add":
    answer = number1 + number2
elif operator == "multiply":
    answer = number1 * number2
elif operator == "divide":
    answer = number1 / number2
else:
    answer = number1 - number2
print(answer)

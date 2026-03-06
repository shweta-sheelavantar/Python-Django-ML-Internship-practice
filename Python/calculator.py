# Simple Calculator Program

a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))
op = input("Enter the operation (+ - * /): ")

if op == "+":
    print(a + b)

elif op == "-":
    print(a - b)

elif op == "*":
    print(a * b)

elif op == "/":
    if b != 0:
        print(a / b)
    else:
        print("Error: Division by zero")

else:
    print("Invalid operation")

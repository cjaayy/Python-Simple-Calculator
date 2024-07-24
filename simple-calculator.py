print("\n\t\t----- SIMPLE CALCULATOR ------\n\n")

print("Enter first number to calculate: ", end = "")
num1 = int (input())

print("\n\n")

print("Enter operator - (+, - , *, /): ", end = "")
calcu = input()

print("\n\n")

print("Enter second number tp calculate: ", end = "")
num2 = int (input())

print("\n\n")

if calcu == "+":
    print("Result: ", end = "")
    print(num1, end = "")
    print(" + ", end = "")
    print(num2,  end = "")
    print(" = ", end = "")
    print(num1 + num2)

elif calcu == "-":
    print("Result: ", end = "")
    print(num1, end = "")
    print(" - ", end = "")
    print(num2,  end = "")
    print(" = ", end = "")
    print(num1 - num2)

elif calcu == "*":
    print("Result: ", end = "")
    print(num1, end = "")
    print(" * ", end = "")
    print(num2,  end = "")
    print(" = ", end = "")
    print(num1 * num2)

elif calcu == "/":
    if num2 != 0:
       print("Result: ", end = " ")
       print(num1, end = "")
       print(" / ", end = "")
       print(num2,  end = "")
       print(" = ", end = "")
       print(num1 / num2)
    else:
     print("\tCannot divide by zero!")
     
else:
    print("\nInvalid!")

print("\n\n")
def addition(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y == 0:
        return "Error! Division by Zero"
    else:
        return x / y 
#user input

print("Enter a number:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice 1/2/3/4 >:")

num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

if choice == "1":
    print(f"The result is >: {add(num1, num2)}")

elif choice == "2":
    print(f"The result is >: {subtract(num1, num2)}")

elif choice == "3":
    print(f"The result is >:{multiply(num1, num2)}")

elif choice == "4":
    print(f"The result is >:{divide(num1, num2)}")

else: print("Error! Please insert a valid number 1/2/3/4")



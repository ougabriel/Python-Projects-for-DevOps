Here are a few simple Python apps for beginners, each with its code. These apps cover a variety of basic concepts such as input/output, loops, conditionals, and simple data structures.

### 1. Calculator
A basic calculator that can perform addition, subtraction, multiplication, and division.

```python
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print(f"The result is: {add(num1, num2)}")
elif choice == '2':
    print(f"The result is: {subtract(num1, num2)}")
elif choice == '3':
    print(f"The result is: {multiply(num1, num2)}")
elif choice == '4':
    print(f"The result is: {divide(num1, num2)}")
else:
    print("Invalid input")
```

### 2. Number Guessing Game
A simple game where the user has to guess a randomly generated number within a certain range.

```python
import random

number_to_guess = random.randint(1, 100)
number_of_attempts = 0

print("Guess the number between 1 and 100")

while True:
    guess = int(input("Enter your guess: "))
    number_of_attempts += 1

    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number in {number_of_attempts} attempts.")
        break
```

### 3. To-Do List
A simple command-line to-do list application where users can add, view, and remove tasks.

```python
to_do_list = []

def show_menu():
    print("\nMenu:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Quit")

def add_task():
    task = input("Enter a new task: ")
    to_do_list.append(task)
    print(f"Task '{task}' added.")

def view_tasks():
    if not to_do_list:
        print("No tasks in the list.")
    else:
        print("\nTasks:")
        for i, task in enumerate(to_do_list, 1):
            print(f"{i}. {task}")

def remove_task():
    view_tasks()
    task_number = int(input("Enter the task number to remove: "))
    if 1 <= task_number <= len(to_do_list):
        removed_task = to_do_list.pop(task_number - 1)
        print(f"Task '{removed_task}' removed.")
    else:
        print("Invalid task number.")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
```

### 4. Simple Contact Book
A basic contact book where users can add, view, and delete contacts.

```python
contacts = {}

def show_menu():
    print("\nMenu:")
    print("1. Add contact")
    print("2. View contacts")
    print("3. Delete contact")
    print("4. Quit")

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    contacts[name] = phone
    print(f"Contact '{name}' added.")

def view_contacts():
    if not contacts:
        print("No contacts in the book.")
    else:
        print("\nContacts:")
        for name, phone in contacts.items():
            print(f"Name: {name}, Phone: {phone}")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.")
    else:
        print("Contact not found.")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        delete_contact()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
```

These simple Python applications are great starting points for beginners to learn the basics of Python programming and understand how to structure a small program.
import random


# This tool lets the user guess a secret number.
def number_guessing_game():
    secret_number = random.randint(1, 10)

    print("\n--- Number Guessing Game ---")
    print("I am thinking of a number between 1 and 10.")

    while True:
        try:
            guess = int(input("Enter your guess: "))

            if guess == secret_number:
                print(f"Correct! The secret number was {secret_number}.")
                break
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")

        except ValueError:
            print("Please enter a whole number.")


# This tool allows the user to add, view, and remove tasks.
def todo_list():
    tasks = []

    print("\n--- To-Do List ---")

    while True:
        print("\n1. Add task")
        print("2. View tasks")
        print("3. Remove task")
        print("4. Return to main menu")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter a task: ")
            tasks.append(task)
            print(f"Task '{task}' was added successfully.")

        elif choice == "2":
            if len(tasks) == 0:
                print("Your to-do list is empty.")
            else:
                print("\nYour tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "3":
            if len(tasks) == 0:
                print("There are no tasks to remove.")
            else:
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

                try:
                    task_number = int(input("Enter the task number to remove: "))

                    if 1 <= task_number <= len(tasks):
                        removed_task = tasks.pop(task_number - 1)
                        print(f"Task '{removed_task}' was removed.")
                    else:
                        print("That task number does not exist.")

                except ValueError:
                    print("Please enter a valid task number.")

        elif choice == "4":
            print("Returning to the main menu.")
            break

        else:
            print("Sorry, that option is not available.")


# This tool performs basic arithmetic calculations.
def calculator():
    print("\n--- Simple Calculator ---")

    try:
        first = float(input("Enter the first number: "))
        operator = input("Enter an operation (+, -, *, /): ")
        second = float(input("Enter the second number: "))

        if operator == "+":
            result = first + second
        elif operator == "-":
            result = first - second
        elif operator == "*":
            result = first * second
        elif operator == "/":
            if second == 0:
                print("Sorry, you cannot divide by zero.")
                return
            result = first / second
        else:
            print("Sorry, that operation is not supported.")
            return

        print(f"Result: {first} {operator} {second} = {result}")

    except ValueError:
        print("Please enter valid numbers.")


# This tool formats the user's name in a friendly way.
def name_formatter():
    print("\n--- Name Formatter ---")

    name = input("Enter your full name: ")
    formatted_name = name.strip().title()

    if formatted_name:
        print(f"Hello, {formatted_name}! Your name looks great.")
    else:
        print("You did not enter a name.")


# Main menu that lets the user choose and run a toolkit.
def main():
    print("================================")
    print("Welcome to My Python Toolkit!")
    print("================================")

    while True:
        print("\n==============================")
        print("1. Number Guessing Game")
        print("2. To-Do List")
        print("3. Simple Calculator")
        print("4. Name Formatter")
        print("5. Quit")
        print("==============================")

        choice = input("Choose a tool: ")

        if choice == "1":
            number_guessing_game()

        elif choice == "2":
            todo_list()

        elif choice == "3":
            calculator()

        elif choice == "4":
            name_formatter()

        elif choice == "5":
            print("Thanks for using My Python Toolkit. Goodbye!")
            break

        else:
            print(f"Sorry, '{choice}' is not a valid choice. Please choose 1-5.")


main()
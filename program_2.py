#Elliott Morris, 1/29/2026, Math Quiz
import random

def addition_quiz():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    answer = int(input(f"What is {num1} + {num2}? "))

    if answer == num1 + num2:
        print("That is Correct")
    else:
        print ("That is incorrect")
        print(f"The correct answer was {num1 + num2}")

def subtraction_quiz():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    answer = int(input(f"What is {num1} - {num2}? "))

    if answer == num1 - num2:
        print("That is Correct")
    else:
        print("That is incorrect")
        print(f"The correct answer was {num1 - num2}")

def multiplication_quiz():
    num1 = random.randint(1, 15)
    num2 = random.randint(1, 15)
    answer = int(input(f"What is {num1} * {num2}? "))

    if answer == num1 * num2:
        print("That is Correct")
    else:
        print("That is incorrect")
        print(f"The correct answer was {num1 * num2}")


def division_quiz():
    num2 = random.randint(1, 15)
    num1 = num2 * random.randint(1, 15)
    answer = int(input(f"What is {num1} / {num2}? "))

    if answer == num1 / num2:
        print("That is Correct")
    else:
        print("That is incorrect")
        print(f"The correct answer was {num1 / num2}")

def main():
    quiz_type = input("Please enter a quiz type (Addition, Subtraction, Multiplication, Division): ").strip().lower()
    if quiz_type == "addition":
        addition_quiz()
    elif quiz_type == "subtraction":
        subtraction_quiz()
    elif quiz_type == "multiplication":
        multiplication_quiz()
    elif quiz_type == "division":
        division_quiz()
    else:
        print("Invalid quiz type")

if __name__ == "__main__":
    main()

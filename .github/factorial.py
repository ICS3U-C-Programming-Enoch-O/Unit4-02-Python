#!/usr/bin/env python3
# Created by: Enoch O
# Created on: March 28, 2025
# This program will calculate the sum of the numbers the user inputs using loop.


def factorial_program():
    # Get user number

    while True:
        try:
            user_number = input("Enter a whole number positive number: ")
            number = int(user_number)
            if number < 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid number, Please enter a whole number.")

    factorial = 1
    i = 1
    while i <= number:
        factorial *= i
        i += 1

    print(f"The factorial of {number} is {factorial}")


if __name__ == "__main__":
    factorial_program()


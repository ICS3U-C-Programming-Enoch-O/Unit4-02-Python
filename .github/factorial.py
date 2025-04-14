#!/usr/bin/env python3
# Created by: Enoch O
# Created on: March 28, 2025
# This program will calculate the sum of the numbers the user inputs using loop.


def main():
    # initializations
    loop_counter = 0
    factorial_answer = 1

    # get the user number
    user_number = int(input("Enter a positive number: "))
    print("")

    # replicates a do..while loop
    # calculate the factorial of the user number using a loop
    while True:
        loop_counter = loop_counter + 1
        factorial_answer = factorial_answer * loop_counter
        print("Tracking {} times through loop.".format(loop_counter))
        if loop_counter >= user_number:
            break

    print("")
    print("{}! = {}".format(user_number, factorial_answer))


if __name__ == "__main__":
    main()

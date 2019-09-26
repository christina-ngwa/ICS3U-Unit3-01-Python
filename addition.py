#!/usr/bin/env python3

# Created by: Christina Ngwa
# Created on: September 2019
# This program calculates the sum of two numbers
#   with user input


def main():

    # this function calculates the sum of two numbers

    # input
    print("Let's find the sum of two integers!")
    print("")
    firstnumber = int(input("Enter the first number (integer): "))
    secondnumber = int(input("Enter the second number (integer): "))

    # process
    total = firstnumber + secondnumber

    # output
    print("")
    print("{0} + {1} = {2}".format(firstnumber, secondnumber, total))


if __name__ == "__main__":
    main()

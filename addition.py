#!/usr/bin/env python3

# Created by: Christina Ngwa
# Created on: September 2019
# This program calculates the sum of two integers
#   with user input


def main():

    # this function calculates the sum of two integers

    # input
    print("Let's find the sum of two integers!")
    print("")
    firstinteger = int(input("Enter the first number (integer): "))
    secondinteger = int(input("Enter the second number (integer): "))

    # process
    total = firstinteger + secondinteger

    # output
    print("")
    print("{0} + {1} = {2}".format(firstinteger, secondinteger, total))


if __name__ == "__main__":
    main()

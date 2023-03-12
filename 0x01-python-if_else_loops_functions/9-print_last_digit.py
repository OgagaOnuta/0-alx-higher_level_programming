#!/usr/bin/python3
'''Prints the last digit of a number'''

def print_last_digit(number):
    if (number < 0):
        number *= -1
    last_digit = number % 10
    print("{}".format(last_digit), end="")
    return (last_digit)

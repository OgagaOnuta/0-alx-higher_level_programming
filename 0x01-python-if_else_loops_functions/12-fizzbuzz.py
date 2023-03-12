#!/usr/bin/python3
'''Prints the numbers from 1 to 100 separated by a space'''

def fizzbuzz():
    '''For multiples of 3, print Fizz
    For multiples of 5, print Buzz
    For multiples of both 3 and 5, print FizzBuzz
    '''
    for i in range(1, 100):
        if (i % 15 == 0):
            i = "FizzBuzz"
        elif (i % 3 == 0):
            i = "Fizz"
        elif (i % 5 == 0):
            i = "Buzz"
        print("{} ".format(i), end="")

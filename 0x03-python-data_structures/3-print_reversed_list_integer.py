#!/usr/bin/python3
'''Prints all integers of a list in reverse order'''


def print_reversed_list_integer(my_list=[]):
    length = len(my_list)

    for i in range(length):
        print("{:d}".format(my_list[length-(i+1)]))

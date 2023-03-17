#!/usr/bin/python3
'''Prints a matrix of integers'''


def print_matrix_integer(matrix=[[]]):
    length0 = len(matrix)

    for i in range(length0):
        length1 = len(matrix[i])

        for j in range(length1):
            print("{}".format(matrix[i][j]), end="")
            if (j < (length1 - 1)):
                print(" ", end="")
        print()

#!/usr/bin/python3
'''Replace an element of a list at a specific position
without modifying the original list'''


def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    if ((idx > 0) and (idx < len(my_list))):
        new_list[idx] = element
        return (new_list)
    else:
        return (new_list)

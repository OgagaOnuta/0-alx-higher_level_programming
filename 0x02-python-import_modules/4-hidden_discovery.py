#!/usr/bin/python3

if __name__ == "__main__":
    from hidden_4 import *
    i = 0
    while (i < len(dir(hidden_4))):
        print("{}".format(dir(hidden_4)[i]))
        i += 1

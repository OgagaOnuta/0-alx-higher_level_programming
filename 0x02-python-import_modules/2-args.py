#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    num = len(sys.argv)
    if (num == 1):
        print("{} arguments.".format(num - 1))
    elif (num == 2):
        print("{} argument:".format(num - 1))
        print("{}: {}".format((num - 1), sys.argv[1]))
    elif (num > 2):
        print("{} arguments:".format(num - 1))
        i = 1
        while (i < num):
            print("{}: {}".format(i, sys.argv[i]))
            i += 1

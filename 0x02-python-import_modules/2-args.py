#!/usr/bin/python3

if __name__ == "__main__":

    import sys
    args = sys.argv[1:]
    counter = len(args)
    if counter == 0:
        print("{} arguments.".format(counter))
    elif counter == 1:
        print("{} argument:".format(counter))
        print("{}: {}".format(counter, sys.argv[counter]))
    else:
        for i in range(counter):
            print("{} arguments:".format(counter))
            print("{}: {}".format(i + 1, args[i + 1]))


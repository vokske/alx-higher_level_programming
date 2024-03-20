#!/usr/bin/python3

if __name__ == '__main__':
    import sys
    args = sys.argv[1:]
    arg_counter = len(args)
    sum_args = 0
    for i in range(arg_counter):
        sum_args += int(args[i])
    print("{}".format(sum_args))

#!/usr/bin/python3

if __name__ == '__main__':
    import sys
    args = sys.argv[1:]
    sum_args = 0
    for i in range(len(args)):
        sum_args += int(args[i])
    print(sum_args)

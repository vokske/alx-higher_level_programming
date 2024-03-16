#!/usr/bin/python3

def pow(a, b):
    power = 1
    if b == 0:
        return 1
    elif b < 0:
        a = 1 / a
    for _ in range(abs(b)):
        power *= a
    return power

#!/usr/bin/python3

import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    valid_operator = {'+', '-', '*', '/'}

    if operator not in valid_operator:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    if operator == '/' and b == 0:
        print("Error: Division by zero")
        sys.exit(1)

    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a, b)
    elif operator == '/':
        result = div(a, b)

    print(f"{a} {operator} {b} = {result}")

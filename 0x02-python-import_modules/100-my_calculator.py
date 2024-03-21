#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    def calculate:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        operator = sys.argv[2]
        valid_operator = ('+', '-', '*', '/')
        if len(sys.argv) != 4:
            print("Usage: ./100-my_calculator.py <a> <operator> <b>")
            sys.exit(1)
        if operator not in valid_operator:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        elif operator == '+':
            return add(a, b)
        elif operator == '-':
            return sub(a, b)
        elif operator == '*':
            return mul(a, b)
        elif operator == '/':
            return div(a, b)
        result = calculate(a, operator, b)
        print(f"{a} {operator} {b} = {result}")

#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, mul, div, sub
    from sys import argv

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    op = argv[2]
    b = int(argv[3])

    match op:
        case '+':
            print("{:d} {} {:d} = {:d}".format(a, op, b, add(a, b)))
        case '-':
            print("{} {} {} = {}".format(a, op, b, sub(a, b)))
        case '/':
            print("{} {} {} = {}".format(a, op, b, div(a, b)))
        case '*':
            print("{} {} {} = {}".format(a, op, b, mul(a, b)))
        case _:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)

#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    z = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in list(z.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    x = int(sys.argv[1])
    y = int(sys.argv[3])
    print("{} {} {} = {}".format(x, sys.argv[2], y, z[sys.argv[2]](x, y)))
                                                                                
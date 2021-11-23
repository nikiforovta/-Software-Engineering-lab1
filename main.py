import sys

USAGE = "Usage: [-C (default)|-F] degree"


def main():
    if len(sys.argv) == 1:
        print("Error! Not enough arguments")
        print(USAGE)
    elif len(sys.argv) == 2:
        print(9 / 5 * int(sys.argv[1]) + 32)
    elif len(sys.argv) == 3:
        if sys.argv[1] == '-C':
            print(9 / 5 * int(sys.argv[2]) + 32)
        elif sys.argv[1] == '-F':
            print(5 / 9 * (int(sys.argv[2]) - 32))
        else:
            print("Error! Unsupported scale")
            print(USAGE)
    else:
        print("Error! Too many arguments")
        print(USAGE)


if __name__ == '__main__':
    main()

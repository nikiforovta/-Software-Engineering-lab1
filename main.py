import sys

USAGE = "Usage: [-C (default)|-F] degrees"


def main():
    if len(sys.argv) == 1:
        print("Error! Not enough arguments")
        print(USAGE)
    elif len(sys.argv) == 2:
        try:
            print(f"You entered:\t{float(sys.argv[1])} °C")
            print(f"Result:\t{(9 / 5 * float(sys.argv[1]) + 32):.3f} °F")
        except ValueError:
            print("Error! Incorrect argument")
    elif len(sys.argv) >= 3:
        if sys.argv[1] == '-C':
            try:
                for k in range(2, len(sys.argv)):
                    print(f"You entered:\t{float(sys.argv[k])} °C")
                    print(f"Result:\t{(9 / 5 * float(sys.argv[k]) + 32):.3f} °F")
            except ValueError:
                print("Error! Incorrect argument")
        elif sys.argv[1] == '-F':
            for k in range(2, len(sys.argv)):
                try:
                    print(f"You entered:\t{float(sys.argv[k])} °F")
                    print(f"Result:\t{(5 / 9 * (float(sys.argv[k]) - 32)):.3f} °С")
                except ValueError:
                    print("Error! Incorrect argument")
        else:
            try:
                float(sys.argv[1])
                for k in range(1, len(sys.argv)):
                    try:
                        print(f"You entered:\t{float(sys.argv[k])} °F")
                        print(f"Result:\t{(5 / 9 * (float(sys.argv[k]) - 32)):.3f} °С")
                    except ValueError:
                        print("Error! Incorrect argument")
            except ValueError:
                print("Error! Unsupported scale")
                print(USAGE)


if __name__ == '__main__':
    main()

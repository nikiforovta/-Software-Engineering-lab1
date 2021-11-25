USAGE = "Usage: [-C (default)|-F] degrees\n"


def main():
    argv = input(USAGE).split()
    if len(argv) == 0:
        print("Error! Not enough arguments")
        print(USAGE)
    elif len(argv) == 1:
        try:
            print(f"You entered:\t{float(argv[0])} °C")
            print(f"Result:\t{(9 / 5 * float(argv[0]) + 32):.3f} °F")
        except ValueError:
            print("Error! Incorrect argument")
    elif len(argv) >= 2:
        if argv[0] == '-C':
            try:
                for k in range(1, len(argv)):
                    print(f"You entered:\t{float(argv[k])} °C")
                    print(f"Result:\t{(9 / 5 * float(argv[k]) + 32):.3f} °F")
            except ValueError:
                print("Error! Incorrect argument")
        elif argv[0] == '-F':
            for k in range(1, len(argv)):
                try:
                    print(f"You entered:\t{float(argv[k])} °F")
                    print(f"Result:\t{(5 / 9 * (float(argv[k]) - 32)):.3f} °С")
                except ValueError:
                    print("Error! Incorrect argument")
        else:
            try:
                float(argv[0])
                for k in range(0, len(argv)):
                    try:
                        print(f"You entered:\t{float(argv[k])} °C")
                        print(f"Result:\t{(9 / 5 * float(argv[k]) + 32):.3f} °F")
                    except ValueError:
                        print("Error! Incorrect argument")
            except ValueError:
                print("Error! Unsupported scale")
                print(USAGE)


if __name__ == '__main__':
    main()

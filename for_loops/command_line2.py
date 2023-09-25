import sys, getopt

def full_name() -> None:
    first_name: str = None
    last_name: str = None

    argv: str = sys.argv[1:]

    try:
        opts, args = getopt.getopt(argv, "f:l:", ["nombre=", " apellido="])


    except:
        print("Error")
        sys.exit()


    for opt, arg in opts:
        if opt in ['-f', 'nombre']:
            first_name = arg
        elif opt in ['-l', 'apellido']:
            last_name = arg

    print(str(first_name) + " " + str(last_name))

def main():
    full_name()

if __name__ == "__main__":
    main()

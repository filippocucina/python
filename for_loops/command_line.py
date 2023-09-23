import sys, getopt

def full_name():
    first_name = None
    last_name = None

    argv = sys.argv[1:]

    try:
        opts, args = getopt.getopt(argv, "f:l:")

    except:
        print("Error")
        sys.exit()

    for opt, arg in opts:
        if opt in ['-f']:
            first_name = arg
        elif opt in ['-l']:
            last_name = arg


    #print(first_name + " " + last_name)
    print(str(first_name) + " " + str(last_name))


def main():
    full_name()

if __name__ == "__main__":
    main()

import sys

def even_odd_numbers(number):
    if number < 1 or number > 50:
        raise ValueError("Number is incorrect")
        sys.exit()

    for loop in range(50):
        if number / 2:
            print("It is a even number!")
            sys.exit("Program Finished")
        else:
            print("It is an odd number!")
            sys.exit("Program Finished ")

def main(): 
    even_odd_numbers(1)


if __name__ == "__main__":
    main()

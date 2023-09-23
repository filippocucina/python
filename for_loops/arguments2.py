import getopt, sys

list_arguments = sys.argv[1:]
options = "abc:"
long_options = ["A_Message", "B_Message", "C_Message"]

try:

    arguments, values = getopt.getopt(list_arguments, options, long_options)
    

    for currentArgument, currentValue in arguments:

        if currentArgument in ("-a", "--A_Message"):
            print("Message A received")
        elif currentArgument in ("-b", "--B_Message"):
            print("Message B received")
        elif currentArgument in ("-c", "--C_Gessage"):
            print("Message C received")

except getopt.error as err:
    print("Error")
    sys.exit()

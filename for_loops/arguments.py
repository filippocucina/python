import sys

print("Arguments without the script name ", (len(sys.argv)-1))
print("Arguments given ")

for i in range(1, len(sys.argv)):
    print(sys.argv[i])

import sys
    

def fizz_buzz(a, b) -> None:
    for i in range(1, 70):
        if i % a == 0 and i % b == 0:
            print("Fizz and Buzz")

        if i % a == 0:
            print("Fizz")

        if i % b == 0:
            print("Buzz")
        
        print(i)

        
def main() -> None:
    fizz_buzz(3, 5)


if __name__ == "__main__":
    main()
            

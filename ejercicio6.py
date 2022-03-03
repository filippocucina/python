
def run():
    numero = int(input("Escribe Un Numero\n"))
    
    if numero:
        for i in range(numero):
            for y in range(i+1):
                print("*", end="")
            print("")

if __name__ == "__main__":
    run()

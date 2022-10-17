
def run():
    numero = int(input("\nEscribe Un Numero\n"))
    
    if numero:
        for i in range(numero):
            if i > 0:
                print(numero - i)
            


if __name__ == "__main__":
    run()


def run():
    numero_usuario = int(input("Escribe un Numero\n"))

    if numero_usuario:
        if numero_usuario % 2 == 0:
            print("Es Par\n")
        else:
            print("Es Impar\n")



if __name__ == "__main__":
    run()


def run():
    numero_entero = int(input("Escribe un numero entero\n"))

    if numero_entero:
        for i in range(numero_entero):
            if i % 2 != 0:
                print(str(i))
            else:
                print("Es par")
            i + 1

if __name__ == "__main__":
    run()

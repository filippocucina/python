
def hola():
    print("Hola Amiga")

def main():
    numero = int(input("Escribe 1 si quieres invocar la funcion. Escribe 2 si no quieres invocar la funcion"))
    
    if numero == 1:
        hola()
    else:
        raise ValueError("Error!")

if __name__ == "__main__":
    main()

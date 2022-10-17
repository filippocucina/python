:#volumen de un cilindro: v = pi*r+**2 * h
#area de un circulo: pi*r**2


def area_circulo(radio):
    pi = 3.14
    return pi*radio**2
    



def volumen_cilindro(radio, altura):
    return area_circulo(radio)*altura



def main():
    r = int(input("Cuanto es el radio?\n"))
    h = int(input("Cuanto es la altura?\n"))

    print(volumen_cilindro(r,h))

if __name__ == "__main__":
    main()

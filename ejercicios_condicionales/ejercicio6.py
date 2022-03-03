
def main():
    grupo_a = []
    grupo_b = []
    
    for i in range(1,3):
        nombre = input(" Escribe tu nombre: ").lower()
        sexo = input(" Escribe tu sexo: ").lower()
        if nombre[0] < "m" and sexo == "f":
            grupo_a.append(nombre)
        elif nombre[0] > "n" and sexo == "m":
            grupo_a.append(nombre)
        else:
            grupo_b.append(nombre)
    print(grupo_a)
    print(grupo_b)


if __name__ == "__main__":
    main()

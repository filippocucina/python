
def main():
    edad = int(input("\nCuantos Años Tienes?\n"))

    if edad:
        if edad < 4:
            print("Puedes entrar gratis!\n")
        elif edad > 4 and edad <= 18:
            print("Debes pagar 5$")
        elif edad > 18:
            print("Debes pagar 10$")
        else:
            raise ValueError("Erro! Introduce tu edad!")





if __name__ == "__main__":
    main()

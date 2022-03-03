
def run():
    edad_usuario = int(input("Cual es tu edad?\n"))
    ingresos_mensuales = int(input("Cual es tu ingreso mensual?\n"))

    if edad_usuario >= 16 and ingresos_mensuales >= 1000:
        print("Debes tributar!\n")
    else:
        print("No debes tributar\n")



if __name__ == "__main__":
    run()


def run():
    clave = "contraseña"
    
    clave_usuario = str(input("\nEscribe la contraseña\n"))

    if clave_usuario:
        if clave == clave_usuario:
            print("Es la misma contraseña\n")
        else:
            print("La contraseña es incorrecta\n")


if __name__ == "__main__":
    run()

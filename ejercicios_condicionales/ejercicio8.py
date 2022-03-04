
def main():
    dinero_recibir = 2400
    puntuacion_usuario = float(input("\nEscribe tu puntuación. 0.0, 0.4, 0.6 > puntuacion> 0.6\n"))

    if puntuacion_usuario:
        if puntuacion_usuario == 0.0:
            print("Recibiras 2400$, pero no tendras ninguna cantidad extra\n")
            print(str("2400$"))
        elif puntuacion_usuario == 0.4:
            print("Recibiras 2400$ * 0.4!\n ")
            dinero_recibir *= puntuacion_usuario
            print(dinero_recibir)
        elif puntuacion_usuario >= 0.6:
            print("Recibiras 2400$ * 0.6 o > 0.6")
            dinero_recibir *= puntuacion_usuario
            print(dinero_usuario)
        else:
            raise ValueError("Error!")
        


if __name__ == "__main__":
    main()

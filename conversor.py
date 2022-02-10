"""

Conversor de Moneda 

Peso Colombianos
Peso Chileno
Peso Argentino

Le das por Consola -> 1- Que tipo de moneda va a cambiar
                   -> 2- Cuanto dinero va a cambiar
                   -> 3- Cuanto equivale lo que me dio a dolares
"""


#Variables del valor de los pesos
peso_colombiano = 3951.20 # -> $1
peso_chileno = 813.01 # -> $1
peso_argentino = 105.88 # -> $1
dolares_usuario = 0


def main():
    tipo_moneda_usuario = input("Que moneda te gustaria cambiar | 1 - Peso Colombiano | 2 - Peso Argentino | 3 - Peso Chileno  ")
    dolares_comprar = input("Cuantos dolares te gustaria comprar? ")

    if tipo_moneda_usuario == 1:
        dolares_usuario = peso_colombiano * dolares_comprar
        print("Necesitas " + str(dolares_usuario) + " Pesos")

    elif tipo_moneda_usuario == 2:
        dolares_usuario = peso_argentino * dolares_comprar         
        print("Necesitas "+ str(dolares_usuario) + " Pesos")

    elif tipo_moneda_usuario == 3:
        dolares_usuario = peso_chileno * dolares_comprar
        print("Necesitas "+ str(dolares_usuario) + " Pesos")

    else:
        print("Error!")


def run():  
    main()


if __name__ == "__main__":
    run()

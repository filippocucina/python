
#Renta Anual = Ganancia al año de una persona

def main():
    renta_anual = int(input("Escribe Cual Es La tu Renta Anual"))
    
    if renta_anual:
        if renta_anual < 10000:
            print("Tipo de Impositivo es del 5%")
        elif renta_anual >= 10000 or rental_anual <= 20000:
            print("Tipo de Impositivo es del 15%")
        elif renta_anual >= 20000 or renta_anual >= 35000:
            print("Tipo de Impositivo es del 20%")
        elif renta_anual >= 35000 or rental_anual <= 60000:
            print("Tipo de Impositivo es del 30%")
        elif renta_anual > 60000:
            print("Tipo de Impositivo es del 45%")
        else:
            raise ValueError("Error!")
    



if __name__ == "__main__":
    main()

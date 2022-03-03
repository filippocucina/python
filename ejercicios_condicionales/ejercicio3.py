
def run():
    dividendo = int(input("Cuanto es su dividendo?\n"))
    divisor = int(input("Cuanto es su divisor?\n"))
    
    if divisor:
        if divisor != 0:
            print("Resultado: ", int(dividendo/divisor))
        else:
            raise ValueError("Error")


if __name__ == "__main__":
    run()

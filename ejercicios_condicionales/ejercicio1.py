
def run():
    edad = int(input("Escribe Tu Edad\n"))
    
    if edad:
        if edad >= 18:
            print("\nEres mayor de edad")
        else:
            print("\nEres menor de edad")
    
    
    
if __name__ == "__main__":
    run()

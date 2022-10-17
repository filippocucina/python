
def run():
    años_usuario = input("Cuantos Años Tienes?\n\n")
    
    if (años_usuario):
        for x in range(int(años_usuario)):
            print("\nHaz cumplido: " + str(x))

if __name__ == "__main__":
    run()

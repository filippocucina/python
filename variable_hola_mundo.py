"""

Variable que almacene Hola Mundo

"""
import py_compile

def main():  
    variable = "Hola Mundo"
    print(variable)

py_compile.compile("variable_hola_mundo.py")

print(f"1 dias son {24} horas")

def run():
    main()

if __name__ == "__main__":
    run()

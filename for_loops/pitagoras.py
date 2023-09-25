import math


def pitagoras(catetoA, catetoB) -> None:
    hipotenusa = 0;
    hipotenusa = math.sqrt(math.pow(catetoA, 2) + math.pow(catetoB, 2))
    print(f"La hipotenusa es: {hipotenusa}")


def main() -> None:
    catetoA = int(input("Escribe un numero para el cateto A\n"))
    catetoB = int(input("Escribe un numero para el cateto B\n"))
    pitagoras(catetoA, catetoB)
    

if __name__ == "__main__":
    main()

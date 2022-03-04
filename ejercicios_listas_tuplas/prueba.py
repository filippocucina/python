def main():
   materias = [materia for materia in input(" Escribe tus materias: ").split()]
   for materia in materias:
       print(f"Estudias {materia}")

if __name__ == "main":
    main()

def main():
   materias = [materia for materia in input(" Escribe tus materias: ").split()]
   notas = [nota for nota in input("Escribe las notas correspondientes: ").split()]
   for materia in materias:
     for nota in notas:
                 print(f"Estudias {materia} con la nota {nota} ")

if __name__ == "__main__":
    main()

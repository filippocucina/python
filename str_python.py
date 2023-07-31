class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"{self.nombre}, {self.edad} años"

persona1 = Persona("Juan", 30)
print(persona1) # Salida: Juan, 30 años


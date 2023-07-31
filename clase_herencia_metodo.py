class ClasePadre:
    def metodo(self):
        print("Este es el método de la clase padre")

class ClaseHija(ClasePadre):
    def metodo(self):
        print("Este es el método de la clase hija")
        super().metodo()

objeto = ClaseHija()
objeto.metodo()


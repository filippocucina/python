
#list comprehensions
#diccionarios = diccionario = {'nombre' : 'Carlos', 'edad' : 22, 'cursos': ['Python','Django','JavaScript'] }

def main():
    numeros = [1,2,3,4,5,6,7,8,9,10]

    pares = [i for i in numeros if i %2 == 0]
    print(pares)


    diccionario = {"nombre" : "Carlos", "edad" : 22, "cursos": ["Python", "Django", "JavaScript"]}

    print(diccionario['nombre']) #Carlos
    print(diccionario['edad'])#22
    print(diccionario['cursos']) #['Python','Django','JavaScript']


    
    
    
if __name__ == "__main__":
    main()

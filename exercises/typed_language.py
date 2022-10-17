#Strongly Typed Language

#name = "Filippo" + 20   # --> retornara un error por que hay que usarlo con la funcion str()
import py_compile

name = "Filippo " + str(20)
print(name)


#Dynamically Language
age = 10

print(type(age))

#Case Sensitive Language
salary = 34.56
Salary = 2000
print(Salary) #Notice how it outputs the variable 'Salary', instead of salary
py_compile.compile("typed_language.py")

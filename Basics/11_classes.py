# Classes


#  para definir una clase por lo general usamos Camelcase y snakecase
from os import name


class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

# def __init__self es un constructor
class Person:
    def __init__(self,name,surname): #init sirve para establecer ciertos valores asociados a personas 
        self.name = name
        self.surname = surname  
#  con Self. estamos definiendo las propiedades del objeto en este caso el objeto persona
# Ahora definiendo las propiedades podemos acceder desde afuera a estas 
my_person = Person("Hector", "Gomez") #asi como las funciones aca las clases tambien necesita que le pasemos argumentos
print(f"{my_person.name} {my_person.surname}") # de esta manera accedemos a la persona que pertenece a la clase Person con las propiedades de nombre y apellido


class PersonFull:
    def __init__(self,name,surname):
        self.full_name = (f"{name} {surname}")
    def walk(self):
        print(f"{self.full_name} esta caminando")

my_full_person = PersonFull("Michelle","Macuare")
print(my_full_person.full_name)
my_full_person.walk() # aca llamamos a la funcion de la clase que es la propiedad que le asignamos "walk" de caminar de esta manera podemos crear funciones asociadas a un objeto en especifico


class Username:
    def __init__(self,name,surname,id,username):
        self.__id = id # __propiedad de esta forma con los dos guiones bajos podemos decirle que es una propiedad privada o una variable privada, es decir el usuario no puede acceder a estos datos
        self.__name = name
        self.__surname = surname #propiedad privada
        self.full_name = f"{name} {surname}"
        self.username = username #propiedad publica
    def get_name(self):
        return self.__name # de esta manera si podemos acceder al nombre pero no podemos hacerle cambios

    def walk(self):
        print(f"{self.full_name} esta caminando")

my_username = Username("Hector","Gomez",67,"hectorluisgm")
print(my_username.full_name)
# print(my_username.__id) #AttributeError: 'Username' object has no attribute 'id', nos devuelve error es defir no podemos acceder a el porque es privado
print(my_username.get_name())




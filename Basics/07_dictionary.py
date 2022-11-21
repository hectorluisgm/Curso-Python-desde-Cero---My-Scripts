# Diccionarios 

# Asi definimos un diccionario 

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

# Los diccionarios son un ripo de estructura que podemos almacenar datos de tipo Clave:Valor
# Un diccionario tambien lo conocemos como un archivo .json 

my_dict = {"Nombre":"Hector", "Apellido":"Gomez", "Edad":23, 1:"Pyhton"}
print(my_dict)

# Dentro de una clave podemos almacenar un Set el cual tiene distintos valores
my_other_dict ={
    "Nombre":"Hector",
    "Apellido":"Gomez",
    "Edad": 23,
    "Lenguajes" : {"Python","C#","Java"},
    1: 1.72
}
print(my_other_dict)

# Con diccionarios Tenemos formas muy faciles de acceder a elementos por ejemplo:
print(my_other_dict["Nombre"])

# Podemos acceder a una clave y cambiarla
my_other_dict["Nombre"] = "Pedro"
print(my_other_dict["Nombre"])

# Podemos agregar clave y valor
my_other_dict["Calle"] = "Av.Cramer"
print(my_other_dict)

# Podemos borrar claves
del my_other_dict["Calle"]
print(my_other_dict)

# El metodo in no nos sirve para buscar si existen valores pero si para las claves
# print("Hector" in my_other_dict)
print("Nombre" in my_other_dict) #Con las claves si funciona

# print("Nombre":"Hector" in my_other_dict) #SyntaxError: invalid syntax
# print({"Nombre":"Hector"} in my_other_dict) #TypeError: unhashable type: 'dict'

# Algunas FUNCIONES 
# .items() nos regresa todos los datos
print(my_other_dict.items()) #dict_items([('Nombre', 'Pedro'), ('Apellido', 'Gomez'), ('Edad', 23), ('Lenguajes', {'C#', 'Java', 'Python'}), (1, 1.72)])
# .values() nos refresa todos los valores
print(my_other_dict.values()) #dict_values(['Pedro', 'Gomez', 23, {'C#', 'Java', 'Python'}, 1.72])
# .keys() nos regresa todas las claves
print(my_other_dict.keys()) #dict_keys(['Nombre', 'Apellido', 'Edad', 'Lenguajes', 1])

# Diccionario vacio .fromkeys
# Podemos pasar de una lista a un Diccionario vacio
my_list = ["Nombre", "Apellido", "Edad"]
my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)

# De misma forma podemos hacer esto sin necesidad de una lista
my_dict_copy = dict.fromkeys(("Nombre","Apellido","Edad"))
print(my_dict_copy)

# Llamamos a otro diccionario y creamos uno vacio con las mismas claves 
my_dict_copy = dict.fromkeys(my_other_dict)
print(my_dict_copy)

# los valores de un Diccionario son Dato de tipo <class 'dict_values'>
my_values = my_other_dict.values()
print(type(my_values))
print(my_values)


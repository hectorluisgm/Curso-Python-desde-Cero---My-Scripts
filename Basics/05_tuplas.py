# Tuplas/ Tuples 

'''
Las tuplas a diferencia de las listas son estructuras inmutables, 
es decir, si nosotros deseamos modificar una tupla la mejor forma es 
convertirla en una lista modificarla y luego volver a convertirla una tupla
Las tuplas son estructuras constantes que no deberian ser cambiadas, si necesitamos
una estructura mutable entonces debemos hacer uso de una lista y no una tupla
'''

# Asi definimos una TUPLA
my_tuple = tuple()
my_other_tuple = ()

my_tuple = ('cambur', 'parchita','lechoza','ocumo', 'ocumo chino', 'ñame' )
print(my_tuple)
print(type(my_tuple))

my_other_tuple = (23,1.72,"Hector","Gomez","hectorluisgm")
print(my_other_tuple)

print(my_tuple + my_other_tuple) # Esto no nos genera ningun error


# del my_other_tuple
# print(my_other_tuple) NameError: name 'my_other_tuple' is not defined

# my_other_tuple.insert(0,"Naranja") # AttributeError: 'tuple' object has no attribute 'insert'
# print(my_other_tuple)

# Como podemos ver las tuplas al intentar modificarlas nos devuelven IndexErrors 


# Para modificar las tuplas debemos convertirlas a listas
# EJEMPLO

# Syntax
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)
print(lst)
# Aca podemos ver como modificamos la tupla a lista y le agregamos un elemento
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')

# Podemos Verificar si un elemento esta dentro de la tupla con el uso de "in"

tpl = ('item1', 'item2', 'item3','item4')
print("item3" in tpl) #True

fruits_new = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits_new) # True
print('apple' in fruits_new) # False
# fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment
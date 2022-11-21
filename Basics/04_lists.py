
# Listas 
# Es un array un poco mas inteligente, asi se definen las listas
# en las listas no es obligatorio usar el mismo tipo de dato, en los arrays si, veremos un ejemplo mas abajo
my_list = list()

my_other_list = []

print(len(my_list))


my_list = [34,56,34,23,65,34]
my_copy_list_numbers = my_list.copy()

my_other_list = [23, 1.72, "Hector", "Gomez"]
print(my_other_list)

# Podemos elegir el indice del elemento de la lista que querramos imprimir ejemplo:
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1]) # con los valores negativos recorremos la lista en reversa 
print(my_other_list[-3])
print(my_other_list.count("Gomez")) #retorna el numero de incidencias de un valor
print(my_list.count(34)) 


# Index errors
# print(my_other_list[4]) # esto nos devuelve error "Fuera de rango" IndexError
# print(my_other_list[-5]) # esto nos devuelve error "Fuera de rango" IndexError

# Podemos definir una variable a cada valor de la lista en una sola linea de codigo
age, height, name, surname = my_other_list
print(name)

name, surname, age, height = my_other_list[2], my_other_list[3], my_other_list[0], my_other_list[1]
print(name) # DE esta otra manera podemos asignarle los valores a mano indicandoles el indice de cada valor ESTO POSIBLEMENTE ES UN FOCO DE ERRORES NORMALMENTE NO SE UNA

# Concatenar listas
print(my_list + my_other_list)

# Como modificar las listas desde afuera
my_other_list.append("hectorluisgomezmoya@gmail.com")
print(my_other_list)

my_other_list.insert(0, "Naranja")
print(my_other_list)

my_list.remove(34) #remueve un  solo elemento , asi esten repetidos en el array , remueve solo el primer elemento que asignamos
print(my_list)

del my_list[0] #para eliminar un elemento de la lista indicandole el indice 
print(my_list)

my_list.pop() #remueve el ultimo elemento de la lista
print(my_list) 

my_list.pop(1) # remueve o desapila de la lista el elemento que pertenece al indice que le indicamos
print(my_list) 
my_pop_element = my_list.pop(1)
print(my_pop_element)

# Podemos copiar listas , el metodo .copy() copia todo el objeto
my_new_list = my_other_list.copy()
my_other_list.clear()
print(my_other_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

# Ordenar listas con .sort
my_copy_list_numbers.sort()
print(my_copy_list_numbers)

#SubListas
print(my_copy_list_numbers[1:3])
print(my_copy_list_numbers[0:3])

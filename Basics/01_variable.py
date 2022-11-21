# Variables

# Las variables se pueden definir como quieran, pero existe una convencion,
# todas las letras deben ser minusculas o con snakecase ej: my_variable = "Algo"
# Asi definimos he inicializamos una variable

from distutils.command.build_scripts import first_line_re


my_string_variable = "My string variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)
# Funcion str de python, sirve para cambiar el tipo de dato a tipo String
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Si podemos concatenar las variables he imprimirlas por consola
# Concatenacion de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de: ", my_bool_variable," variable booleana")


#  Funciones del sistema 

# Len() nos devuelve la longitud
print(len(my_string_variable))

# Variables en una sola linea / esto aunque se pueda hacer no es muy buena practica
name, surname, alias, age = "Hector", "Gomez", "toto", 23
print("Hola mi nombre es,", name,surname,"pero tambien me llaman", alias,"y mi edad es", age) 

# Inputs
name = input("Cual es tu nombre?") 
age = input("Cual es tu edad?")

print(name)
print(age) 

# Pyhton es un lenguaje de tipado debil es decir no se debe especificar el tipo de dato de la variable
# Sin embargo pordemos especificar el tipo, pero no lo hace estrictamente

# Forzamos el tipo?
address: str = "Av Cramer 1783"
address = 84
print(type(address)) #  Aca podemos notar que el tipo ha sido cambiado por lo tanto especificar el tipo solo nos sirve de manera visual





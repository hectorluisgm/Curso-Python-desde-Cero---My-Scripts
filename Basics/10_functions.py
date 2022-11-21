# Functions

# Asi definimos una funcion en python 
def my_function():
    print("Esto es una funcion")
# Aca llamamos a la funcion para que se ejecute 
my_function()
# En python las funciones no usan [] ni {} para denotar donde empieza y donde termina, solo con tabular
# debajo de donde definimos la funcion inclye esto como parte de la misma 

def funcion_suma (first_value,second_value): #dentro de () pasamos los parametros
    print(first_value + second_value)

funcion_suma(8,5) # Aca llamamos a la funcion y debemos indicarle los argumentos
funcion_suma(1.8, 1.2)
funcion_suma("Hola", " Python") # Con esta funcion Suma tambien podemos concatenar strings 

# Pyhton es un lenguaje de tipado dinamico podemos ingresarle tanto Int , Float y Strings en esta funcion sin ningun error en el sistema

# Tambien podemos retornar valores reales con Return

def my_function_with_return(first_value:int, secont_value):
    return first_value + secont_value

my_function_with_return(7,2) # llamamos a la funcion de esta manera pero no recibimos ningun valor para ello devemos asignarle ese retorno a una variable

my_result = my_function_with_return(1.7,2.8)
print(my_result)
my_result = funcion_suma(8,2)
print(my_result) # Nos retorna None ya que en la funcion_suma() no retornamos ningun valor explicitamente


def print_name(name, surname):
    print(f"{name} {surname}") # De esta forma podemos pasar variables dentro de un string 

print_name(surname="Gomez", name="Hector") #llamamos a la funcion especificandole los parametros a los argumentos
# Hector Gomez retorno


def print_name(name, surname, alias = "Sin Alias"): #Podemos asignarle valores por defecto danole un valor al parametro (alias = "Sin Alias") 
    print(f"{name} {surname} {alias}")

print_name("Hector", "Gomez")

def print_upper_text(*texts): #asignandole '*' estamos indicandole que pueden ser multiples parametros 
    for element in texts:
        print(element.upper())

print_upper_text("hola", "manzana","python","algebra")


# AttributeError: 'tuple' object has no attribute 'upper'
# recordar que debemos darle el valor de el elemento para que vaya haciendo cada uno si le damos el parametro nos lo toma como una tupla


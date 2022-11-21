# Strings

my_string = "Este es un String"

my_other_string = "Este es otro String"

print(my_string)
print(my_other_string)
print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de linea" # se usa \n para hacer un salto de linea
print(my_new_line_string)

my_tab_line_string = "\t Este es un String tabulado"
print(my_tab_line_string)

# Formateo

name, surname, age = "Hector", "Gomez", 23

print("Mi nombre es {} {} y mi edad {}".format(name,surname,age))
print("Mi nombre es %s %s y mi edad %d"%(name,surname,age)) # %s para str y %d para int

print("Mi nombre es " + name + " " + surname + " y mi edad " + str(age)) # de esta manera logramos lo mismo pero es mucho mas largo y debemos cambiar el tipo de dato de una variable para que funcione de las otras dos no 


print(f"Mi nombre es {name} {surname} y mi edad {age}") # Esta es de las formas mas limpias de formatear

# Desempaquetado de caracteres 

language = "python"
a,b,c,d,e,f = language

print(a)
print(b)

# Division de caracteres 

language_slice = language[0:2] # en este lenguaje recorre las letras por la cantidad de espacio que demos entre los numeros es decir 0:1 nos devuelve la primera letra 0:2 nos devuelve las primeras 2 letras, siempre se cuentan desde el 0
print(language_slice)

language_slice = language[1:] # Esto nos imprime desde el indice de la letra que seleccionamos hasta la ultima
print(language_slice)

language_slice = language[-2] # Usando numero negativos nos devuelve las letras en reversa
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reverse 

language_slice = language[::-1] # Nos devuelve la palabra al revez
print(language_slice)

# Funciones 

print(language.capitalize())
print(language.upper())
print(language.count("p"))
print(language.isnumeric())
print("5".isnumeric()) # Asi sea un dato tipo string la funcion .isnumeric nos devuelve que "5" es True
print(language.lower()) # convierte todas las letras a minuscula

print(language.upper().isupper()) # .isupper() para evaluar si el string esta todo en MAYUSCULA
print(language.lower().isupper())

print(language.startswith("py"))






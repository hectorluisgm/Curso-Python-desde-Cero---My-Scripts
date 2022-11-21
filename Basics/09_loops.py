# Bucles/Loops


# While / Mientras Que

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: #es opcional
    print("Mi condicion es mayor o igual que 10")


while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Mi condicion es igual a 15, se detendra la ejecucion")
        break # con Break podemos detener la ejecucion del bucle
    print(my_condition)



print("La ejecución continúa")

# For / bucle = Para

my_list = [34,56,34,23,65,34]

for element in my_list: # Bucle for es un bucle finito de esta manera podemos recorrer los elementos de una lista o estructura de multiples valores
    print(element)

my_tuple = ('cambur', 'parchita','lechoza','ocumo', 'ocumo chino', 'ñame' )
for frutas in my_tuple:
    print(frutas)

my_dict = {"Nombre":"Hector", "Apellido":"Gomez", "Edad":23, 1:"Pyhton"}

for element in my_dict:
    if element == "Edad":
        print(my_dict.values())
        break
    print(element) #en este caso con un dicionario imprime las claves mas no los valores


for element in my_dict:
    print(element)
    if element == "Edad":
        continue # no se usa es situacional , continue nos regresa al principio del bucle sin pasar a siguiente linea
    print("Se ejecuta")



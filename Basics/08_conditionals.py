# CONDICIONALES


my_condition = False

if my_condition: #es lo mismo que if my_condition == True 
    print("Se a cumplido la condicion")


my_condition = 1
if my_condition > 10 and my_condition < 20:
    print("La variable es mayor que 10 y menos que 20")
elif my_condition == 1:
    print("La Variable es 1")
else:
    print("La variable es menor o igual que diez o mayor o igual que 20")

# if my_condition: esto es lo mismo que if my_condition == True , lo cual es redundante por eso se escribe solo con los dos puntos porque se espera que la condicion siempre sea verdadera


# Una cadena de texto vacia por defecto nos indica boolean Falso
my_string = ""

if my_string:
    print("El strin NO esta vacio")
else:
    print("El String esta vacio")

# Otra forma de comprobar si el String es vacio podria ser 
if not my_string:
    print("La variable esta Vacia")

print("La ejecucion continua")

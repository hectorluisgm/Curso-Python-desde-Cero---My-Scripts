# SETS
# NO SON ESTRUCTURAS INMUTABLES, al igual que las listas podemos agregar elementos pero no podemos acceder a su indice 
# Como definimos sets
my_set = set()
# o
my_other_set = {}

# pero
print(type(my_set))
print(type(my_other_set)) #<class 'dict'> aca tenemos una incongruencia , nos dice que es tipo diccionario 
# pero
my_other_set = {"Hector", "Gomez", 23}
print(my_other_set) #{'Gomez', 'Hector', 23}
print(type(my_other_set)) #<class 'set'> aca despues de haberle dado valores al Set nos dice que es en efecto un set 


print(len(my_other_set)) # 3


# print(my_other_set[0]) TypeError: 'set' object is not subscriptable 

my_other_set.add("hectorluisgm")
print(my_other_set) # Un set no es una estructura ordenada, al ingresar un elemento nos deveulve una lista desordena

my_other_set.add("hectorluisgm") # Un set no admite elementos repetidos 
print(my_other_set)

print("Gomez" in my_other_set) #True
print("Gpmez" in my_other_set) #False

my_other_set.remove(23) #Nos permite remover elementos a diferencia de las tuplas que no es posible
print(my_other_set)



# print(my_set + my_other_set) TypeError: unsupported operand type(s) for +: 'set' and 'set'

my_other_set.clear() #Si nos deja limpiar la lista
print(len(my_other_set))

del my_other_set
# print(my_other_set) Nos dice que no esta definido porque hemos borrado la variable


# De Esta forma convertimos un SET  en una LISTA 
# PERO no es conveniente ya que los SETS son estructuras desordenadas por lo tanto cuando deseemos acceder a un indice de la lista siempre va cambiar su posicion 
my_set = {"Hector", "Gomez", 23}
my_list = list(my_set)
print(my_list)
print(my_list[0])


my_other_set = {"Javascript", "Html","CSS"}
print(my_set.union(my_other_set))

my_new_set = my_set.union(my_other_set)
print(my_new_set)
# Aca  vemos que con .union() podemos juntar sets , en este caso de abajo estamos repitiendo elementos 
# con sets anteriores, por lo tanto el lenguaje evita los anteriores y solo le suma el nuevo set {"Python", "Java", "C#"}
print(my_new_set.union(my_new_set).union(my_set).union({"Python", "Java", "C#"}))

print(my_new_set.difference(my_set)) # Podemos imprimir la diferencia entre dos Sets





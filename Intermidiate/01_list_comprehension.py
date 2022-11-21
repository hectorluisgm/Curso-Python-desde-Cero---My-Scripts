### List Comprehension ###

my_original_list = [56,23,745,23,86,12,237,34]



my_list = [i for i in my_original_list]
print(my_list)
#Tres maneras de crear la misma lista, una a mano, otra con funcion list() y por ultimo con un bucle for
my_original_list = [0,1,2,3,4,5,6,7]
print(my_original_list)

#Range()
my_range = range(8)
print(list(my_range))

my_list = [i + 1 for i in range(8)]
print(my_list)

def sum_Five(number):
    return number + 5

my_list = [sum_Five(i) for i in range(8)] #Podemos ingresarle funciones al bucle que rellena nuestra lista de esta forma
print(my_list)








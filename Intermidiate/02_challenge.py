### CHALLENGE ###

#Escribe un programa que muestre por consola (con un print) los
#números de 1 a 100 (ambos incluidos y con un salto de línea entre
# cada impresión), sustituyendo los siguientes:
# - Múltiplos de 3 por la palabra "fizz".
#- Múltiplos de 5 por la palabra "buzz".
# - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".


def fizzbuzz():
    for index in range(101):

        if index % 3 == 0 and index % 5 == 0:
            index = "fizzbuzz"
        elif index % 3 == 0:
            index = "fizz"
        elif index % 5 == 0:
            index = "buzz"
        else:
            index
        print(index)

fizzbuzz()

# ANAGRAMA
#  * Escribe una función que reciba dos palabras (String) y retorne
#  * verdadero o falso (Bool) según sean o no anagramas.
#  * - Un Anagrama consiste en formar una palabra reordenando TODAS
#  *   las letras de otra palabra inicial.
#  * - NO hace falta comprobar que ambas palabras existan.
#  * - Dos palabras exactamente iguales no son anagrama.

palabra = "palabra"
print(sorted(palabra))
# sorted() esta funcion nos separa letra por letra una palabra de manera ordenada en una lista 

def is_anagram(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    return sorted(word_one.lower()) == sorted(word_two.lower())

print(is_anagram('Amor','Roma'))


#SUCESION DE FIBONACCI
#  * Escribe un programa que imprima los 50 primeros números de la sucesión
#  * de Fibonacci empezando en 0.
#  * - La serie Fibonacci se compone por una sucesión de números en
#  *   la que el siguiente siempre es la suma de los dos anteriores.
#  *   0, 1, 1, 2, 3, 5, 8, 13...

def fibonacci():
   numero_previo = 0
   numero_siguiente = 1
   for index in range(0,51):
       print(numero_previo) # este print va al principio para asegurarnos que empiece desde 0

       fibo = numero_previo + numero_siguiente # 0+1
       numero_previo = numero_siguiente # nprev = 1
       numero_siguiente = fibo # nsig = 0 + 1 = 1 "primera vuelta"

fibonacci()



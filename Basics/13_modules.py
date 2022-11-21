# Modules / Modulos

# La modularizacion del codigo es una manera de ahorrar lineas de codigo, donde definimos un archivo con 
# las variables y funciones que deseamos usar y las importamos al archivo donde lo necesitemos, de esta manera
# ahorramos lineas de codigo y posibles errores que puedan llegar a pasar


# De la siguiente manera importamos modulo en python 
# importar valores no admite nombres de fichero que empiecen por numero, por lo general debemos usar nombres claros en minuscula

import module
from module import printValues, sumarValores # De esta otra forma podemos llamar a module pero importando una funcion en especifico 

module.sumarValores(10,9,1) 
module.printValues("HolaPython")

sumarValores(10,9,1) # Para llamar a la funcion ya de esta manera no necesitamos el uso de module. , la llamamos sin mas 

# Al momento de llamar a la funcion se ha escrito automaticamente en la linea de codigo import 
printValues("Se ha importado la funcion correctamente")

# Tambien podemos llamar Modulos que ya estan integrados en python sin que esten dentro de nuestro fichero
import math
# Como ejemplo tenemos el modulo math, y consigo trae muchas funciones matematicas
math.sin()
math.atan()
math.cos()
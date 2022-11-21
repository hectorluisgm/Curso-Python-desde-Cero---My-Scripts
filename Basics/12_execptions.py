# Execptions : Manejo de erroes / Handling  

number_one = 5
number_two = 1
number_two = "1"

# try: except: 
# Con try: y except: podemos evitar que aparezcan errores por consola, y nos tire abajo toda nuestra aplicacion 
try:
    print(number_one + number_two)
except:
    print("Se ha producido un error")

# try: except: else:
try:
    print(number_one + number_two)
    print("Ha funcionado correctamente")
except:
    # Se ejecuta SI se produce la exception 
    print("Se ha producido un error")
else: #Opcional
    # Se ejecuta si no se produce una excepcion 
    print("La ejecucion continua correctamente") 
finally: #Opcional
    # Se ejecuta siempre
    print("La ejecuion continua")

# Excepcion por tipo

try:
    print(number_one + number_two)
except ValueError:
    print("Se ha producido un ValueError")
except TypeError: #de esta manera podemos asignarle el tipo de error especificamente al que va a reaccionar esta excepcion 
    print("Se ha producido un TypeError")

# Captura de la informacion de la excepcion

# Definimos error como un objeto 
try:
    print(number_one + number_two)
    print("Ha funcionado correctamente")
except ValueError as error:
    print(error) #TypeError: unsupported operand type(s) for +: 'int' and 'str' aca capturamos este error 
except Exception as error: #base class Exception es una forma de controlar que sea cual sea el tipo de error lo haga  
    print(error)



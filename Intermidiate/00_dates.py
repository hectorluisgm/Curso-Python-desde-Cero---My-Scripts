from cgi import print_form
from datetime import date, datetime
from datetime import time

now = datetime.now()

print(now.hour)
print(now.minute)
print(now.second)
print(now.day)
print(now.month)
print(now.year)

timestamp = now.timestamp()

print(timestamp)

# def Print_date(date):


#Lo minimo que necesitamos para imprimir un datetime es dia mes y año 

current_time = time(17,14,9) 
#Nos sirve para encapsular tiempo, y debemos rellenarlo.
#Podria servir para atrapar la hora fecha de cuando un usuario se dio de alta en nuestra pagina
# print(current_time) Esto nos tira error a la funcion time() hay que definirle el dato que queremos ingresar como .hour .min
print(current_time.hour)
print(current_time.minute) #a diferencia de datetime para llamar a min debemos hacerlo como .minute
print(current_time.second)

current_date = date.today()  #Asi le podemos definir el dia a date 

print(current_date.year)
print(current_date.month)
print(current_date.day)

# Como cambiamos las fechas de sus valores originales 

current_date = date(current_date.year, current_date.month + 1, current_date.day)

print(current_date.month) #deberia devolver 12 siendo hoy 11 a sumarle 1 
#De esta manera poco eficiente podemos cambiar la fecha de cualquiera de las variables

#Si los objetos son del mismo tipo si podriamos add o sustraerlos ejemplo day con day o year con year 

from datetime import timedelta
#TimeDelta nos permite sumar o sustraer estos tipos de datos que serian fechas en si, cuando con las demas clases no podiamos 
start_timedelta = timedelta(200,100,100,weeks= 10) 
end_timedelta = timedelta(300, 100,100,weeks= 13)
print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)










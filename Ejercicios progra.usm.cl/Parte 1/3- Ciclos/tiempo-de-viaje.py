#Variable para el tiempo total de viaje
tiempo_total = 0

#Comenzamos pidiendo una duracion de tramo
duracion = int(raw_input("Duracion tramo: "))

#Mientras la duracion no sea cero...
while (duracion != 0):
	#Sumamos la duracion a nuestro contador
	tiempo_total += duracion
	#Y pedimos la siguiente duracion
	duracion = int(raw_input("Duracion tramo: "))

#Cuando la duracion ingresada sea cero, expresamos
#el tiempo total en horas y minutos
print "Tiempo total del viaje:",str(tiempo_total/60)+":"+str(tiempo_total%60),"horas"
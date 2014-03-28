#Primero, pedimos los datos.
tipo = raw_input("Tipo vehiculo: ")
dia = raw_input("Dia: ")
horario = raw_input("Horario: ")
#Si es auto, pedimos la cantidad de pasajeros
if tipo == "auto":
	pasajeros = int(raw_input("Cantidad pasajeros: "))

#Ahora calculamos el total a pagar.
#Esta depende del dia, hora, tipo de vehiculo y cantidad de pasajeros (si aplica).
if dia == "lunes" or dia == "martes" or dia == "miercoles" or dia == "jueves" or dia == "viernes":
	#Estamos en hora de alta congestion?
	if (horario >= "07:30" and horario <= "09:30") or (horario >= "17:30" and horario <= "20:00"):
		#Alta congestion
		#Autos: $2400, si tiene mas de 3 pasajeros (incluido) no pagan.
		#Camiones pegan $3500
		if tipo == "auto":
			if pasajeros >= 3:
				total = 0
			else:
				total = 2400
		else:
			total = 3500
	else:
		#Baja congestion
		#Autos: $2000 menos $100 por pasajero
		#Camiones: $2500
		if tipo == "auto":
			total = 2000 - 100 * pasajeros
		else:
			total = 2500
else:
	#Sabado o Domingo
	#Estamos en hora de alta congestion?
	if (horario >= "08:30" and horario <= "11:00") or (horario >= "17:45" and horario <= "22:30"):
		#Alta congestion
		#Autos: 4500 menos $300 por pasajero
		#Camiones: $4500
		if tipo == "auto":
			total = 4500 - 300 * pasajeros
		else:
			total = 4500
	else:
		#Baja congestion
		#Autos: $2800
		#Camiones: $3800
		if tipo == "auto":
			total = 2800
		else:
			total = 3800

print "Total a pagar: "+str(total)
def registro_paso_portico(patente, fecha, hora):
	#Abrimos el archivo en modo append
	trafico = open('trafico.dat', 'a')
	#Agregamos la informacion dada al archivo
	#OJO, que la fecha esta como string, no como tupla!
	registro = patente + "," + fecha + "/" + hora
	trafico.write(registro+"\n")

	trafico.close()
	#La funcion no retorna nada
	return None

#Prueba
registro_paso_portico('crtj12', '2014.03.17', '00:57')

def info_facturacion(patente, (fecha1, fecha2)):
	#Primero obtenemos el monto a facturar, basados en el intervalo de fechas y en los niveles de cobro.
	monto_facturado = 0
	trafico = open('trafico.dat')
	#Leemos linea por linea
	for datos in trafico:
		#Limpiamos y separamos
		patente_auto, datos2 = datos.strip().split(",")
		fecha_paso, hora_paso = datos2.split("/")

		#La patente es la buscada? La fecha esta en el rango deseado?
		if (patente == patente_auto) and (fecha1 <= fecha_paso <= fecha2):
			#Veamos a que nivel de cobro corresponde...
			if "00:00" <= hora_paso <= "05:59": #Nivel 1
				monto_facturado += 50
			elif "06:00" <= hora_paso <= "09:59": #Nivel 2
				monto_facturado += 200
			elif "10:00" <= hora_paso <= "16:59": #Nivel 3
				monto_facturado += 100
			elif "17:00" <= hora_paso <= "23:59": #Nivel 4
				monto_facturado += 300

	trafico.close()

	#Ya teniendo el monto a facturar, obtenemos el resto de los datos
	clientes = open("clientes.dat")
	for linea in clientes:
		patente_auto, apellido1, apellido2, nombre, direccion, ciudad = linea.strip().split(",")
		#Es esta la persona buscada?
		if patente_auto == patente:
			#Construimos la tupla a devolver
			datos_cliente = (apellido1, apellido2, nombre, direccion, ciudad, monto_facturado)

	clientes.close()
	return datos_cliente

#Prueba
print info_facturacion('crtj12', ('2014.02.20', '2014.03.19'))

def bolsillo_concesionario((fecha1, fecha2)):
	#Es basicamente lo de funcion anterior, pero sin comprobar patente o datos del cliente.
	monto_facturado = 0
	trafico = open('trafico.dat')
	#Leemos linea por linea
	for datos in trafico:
		#Limpiamos y separamos
		patente_auto, datos2 = datos.strip().split(",")
		fecha_paso, hora_paso = datos2.split("/")

		#La patente es la buscada? La fecha esta en el rango deseado?
		if fecha1 <= fecha_paso <= fecha2:
			#Veamos a que nivel de cobro corresponde...
			if "00:00" <= hora_paso <= "05:59": #Nivel 1
				monto_facturado += 50
			elif "06:00" <= hora_paso <= "09:59": #Nivel 2
				monto_facturado += 200
			elif "10:00" <= hora_paso <= "16:59": #Nivel 3
				monto_facturado += 100
			elif "17:00" <= hora_paso <= "23:59": #Nivel 4
				monto_facturado += 300

	trafico.close()
	#Devolvemos el monto total facturado
	return monto_facturado

#Prueba
print bolsillo_concesionario(('2014.02.27', '2014.03.17'))
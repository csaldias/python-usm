#Los datos del problema.
vuelos = [(10, (2014,01,02)), (11, (2014,01,02)), (12, (2014,01,03)), (13, (2014,05,01)), (14, (2014,05,01))]

destinos = {
	10: {('Lima','Peru'), ('San Jose','Costa Rica'), ('Los Angeles','USA')},
	11: {('San Jose','Costa Rica'), ('C. de Panama','Panama')},
	12: {('Sao Paulo','Brasil'), ('San Jose','Costa Rica')},
	13: {('Lima','Peru'), ('San Jose','Costa Rica'), ('C. de Panama','Panama')},
	14: {('San Jose','Costa Rica'), ('Buenos Aires','Argentina')}
}

#Pregunta a)
def vuelos_a_destino(destino, fecha):
	#Creamos 2 listas auxiliares
	vuelos_fecha = []
	vuelos_destino = []
	#Iteramos sobre la lista de vuelos
	for num_vuelo, fecha_vuelo in vuelos:
		#Si el vuelo sale en la fecha que buscamos...
		if fecha_vuelo == fecha:
			#Lo agregamos a nuestra lista
			vuelos_fecha.append(num_vuelo)

	#Iteramos sobre nuestra lista de vuelos en fecha (vuelos_fecha)
	for num_vuelo in vuelos_fecha:
		#Si el vuelo tiene como uno de sus destinos el solicitado...
		if destino in destinos[num_vuelo]:
			#Lo agregamos a nuestra lista
			vuelos_destino.append(num_vuelo)
	return vuelos_destino

#Pregunta b)
def destinos_repetidos():
	destinos_vuelos = []
	#Iteramos sobre las llaves y valores de destinos
	for codigo_vuelo, destinos_vuelo in destinos.items():
		#Guardamos todos los destinos
		destinos_vuelos.append(destinos_vuelo)
	#Guardamos temporalmente la interseccion de los primeros
	#2 grupos de destinos
	temp = destinos_vuelos[0] & destinos_vuelos[1]
	#Iteramos desde el tercer grupo de destinos en adelante
	for i in range(2,len(destinos_vuelos)):
		#Calculamos los destinos comunes
		destinos_comunes = destinos_vuelos[i] & temp
		#Actualizamos nuestra variable temporal
		temp = destinos_comunes
	return destinos_comunes

#pregunta c)
def paises_visitados(fecha):
	vuelos_fecha = []
	paises = set()
	#Buscamos los vuelos con la fecha pedida
	for num_vuelo, fecha_vuelo in vuelos:
		#Si el vuelo sale en la fecha que buscamos...
		if fecha_vuelo == fecha:
			#Lo agregamos a nuestra lista
			vuelos_fecha.append(num_vuelo)

	#Iteramos sobre vuelos_fecha
	for num_vuelo in vuelos_fecha:
		for ciudad, pais in destinos[num_vuelo]:
			paises.add(pais)

	return paises
#Prueba
print vuelos_a_destino(('San Jose','Costa Rica'), (2014,05,01))

print destinos_repetidos()

print paises_visitados((2014,05,01))
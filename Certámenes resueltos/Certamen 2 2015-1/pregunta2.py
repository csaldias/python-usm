#Lista de Tuplas de la Pregunta 2
cartelera = [
	#(mes, pais, nombre_pelicula, anho_filmacion, [sala1, sala2, ...])
	('febrero', 'FRANCIA', 'El Muelle', 1962, ['sala1', 'sala3']),
	('febrero', 'FRANCIA', 'La Dama de Honor', 2004, ['sala1', 'sala4']),
	('abril', 'RUSIA', 'Padre del Soldado', 1964, ['sala3', 'sala2', 'sala4']),
	('enero', 'CHILE', 'Gloria', 2013, ['sala1', 'sala2']),
	('mayo', 'MEXICO', 'Cumbres', 2013, ['sala3', 'sala2']),
	('julio', 'FRANCIA', 'Melo', 1986, ['sala3', 'sala1']),
	('junio', 'BELGICA', 'Rondo', 2012, ['sala4', 'sala2']),
	('marzo', 'ALEMANIA', 'Tiempo de Canibales', 2014, ['sala1', 'sala2']),
	('marzo', 'ALEMANIA', 'Soul Kitchen', 2009, ['sala3', 'sala4'])
]

#Punto a)
def pelicula_por_pais(cartelera, pais):
	#Nos piden lista, creamos lista
	peliculas_pais = []
	#Recorremos la cartelera
	for mes_exhibicion, pais_pelicula, nombre_pelicula, anho_filmacion, salas in cartelera:
		#Si la pelicula actual fue filmada en el pais que nos interesa...
		if pais_pelicula == pais:
			#Guardamos su nombre y anho de filmacion en una tupla, y la guardamos.
			peliculas_pais.append( (nombre_pelicula, anho_filmacion) )
	#Dejamos que itere, para que obtenga todas las peliculas del pais.
	#Cuando terminamos, devolvemos la lista.
	return peliculas_pais

#Probando, probando...
print pelicula_por_pais(cartelera, 'FRANCIA')

#Punto b)
def peliculas_por_sala(cartelera, sala):
	#Nos piden diccionario, creamos diccionario
	peliculas_sala = dict()
	#Recorremos la cartelera
	for mes_exhibicion, pais_pelicula, nombre_pelicula, anho_filmacion, salas in cartelera:
		#Si la pelicula actual se exhibe en la sala que nos interesa...
		if sala in salas:
			#Agregamos el nombre de la pelicula al diccionario, usando su mes como llave.
			#Si el mes existe en el diccionario...
			if mes_exhibicion in peliculas_sala:
				#Simplemente actualizamos el valor, agregando el nombre de la pelicula a la lista
				peliculas_sala[mes_exhibicion].append(nombre_pelicula)
			#Si el mes no existe en el diccionario...
			else:
				#Lo creamos
				peliculas_sala[mes_exhibicion]=[nombre_pelicula]
	#Dejamos que itere, para que obtenga las peliculas por mes que se exhiben en la sala
	#Cuando terminamos, devolvemos el diccionario
	return peliculas_sala

#Probando, probando...
print peliculas_por_sala(cartelera, 'sala1')

#Punto c)
def mas_antigua(cartelera):
	#Llevamos la cuenta del pais, nombre y anho de la pelicula mas antigua
	anho_mas_antiguo = 9999
	nombre_mas_antiguo = ''
	pais_mas_antiguo = ''
	#Recorremos la cartelera
	for mes_exhibicion, pais_pelicula, nombre_pelicula, anho_filmacion, salas in cartelera:
		#Si la pelicula actual es mas antigua que la pelicula mas antigua conocida...
		if anho_filmacion <= anho_mas_antiguo:
			#Actualizamos los datos de la pelicula mas antigua conocida
			anho_mas_antiguo = anho_filmacion
			nombre_mas_antiguo = nombre_pelicula
			pais_mas_antiguo = pais_pelicula
	#Dejamos que itere, para que obtenga el nombre y pais de la pelicula mas antigua en cartelera
	#Cuando terminamos, devolvemos estos valores en formato tupla
	return (nombre_mas_antiguo, pais_mas_antiguo)

#Probando, probando...
print mas_antigua(cartelera)

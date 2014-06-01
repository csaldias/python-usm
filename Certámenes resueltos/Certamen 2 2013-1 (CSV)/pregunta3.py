#Datos de ejemplo del problema.
jugadores = [
			#(nombre,(posicion,goles,precio))
			('Alexis Sanchez',('delantero',8,14000000)),
			('Arturo Vidal',('central',3,4000000)),
			('Claudio Bravo',('arquero',1,300000)),
			('Gary Medel',('defensa',1,6000000)),
			('Gonzalo Jara',('defensa',1,3000000)),
			('Eugenio Mena',('defenda',0,5000000)),
			('Miguel Pinto',('arquero',1,2000000)),
			('Fabian Orellana',('delantero',3,4000000))
			]

#Pregunta a)
def jugadores_por_posicion(posicion,jugadores):
	jugadores_posicion = set()
	#Iteramos y desempaquetamos
	for nombre, (posicion_juego, _, _) in jugadores:
		#Si la posicion de juego de este jugador es la buscada...
		if posicion_juego == posicion:
			#Agregamos su nombre a nuestro diccionario
			jugadores_posicion.add(nombre)
	return jugadores_posicion

#Pregunta b)
def cantidad_goles(nombre,jugadores):
	#Iteramos sobre jugadores y desempaquetamos
	for nombre_jugador, (_, goles, _) in jugadores:
		#Si el nombre del jugador es el solicitado...
		if nombre_jugador == nombre:
			#Devolvemos la cantidad de goles
			return goles

#Pregunta c)
def cantidad_goles_por_posicion(posiciones,jugadores):
	goles_posicion = {}
	#Iteramos sobre el conjunto posiciones
	for posicion in posiciones:
		#Obtenemos los jugadores que juegan en esta posicion
		jugadores_posicion = jugadores_por_posicion(posicion, jugadores)
		#Otenemos los goles de cada uno
		goles_totales = 0
		for jugador in jugadores_posicion:
			goles_totales += cantidad_goles(jugador, jugadores)
		#Y agregamos los datos al diccionario
		goles_posicion[posicion] = goles_totales
	return goles_posicion


#Prueba
print jugadores_por_posicion('delantero',jugadores)
print jugadores_por_posicion('defensa',jugadores)
print jugadores_por_posicion('arquero',jugadores)

print cantidad_goles('Alexis Sanchez',jugadores)
print cantidad_goles('Eugenio Mena',jugadores)

posiciones = {'arquero','defensa','central','delantero'}
print cantidad_goles_por_posicion(posiciones,jugadores)
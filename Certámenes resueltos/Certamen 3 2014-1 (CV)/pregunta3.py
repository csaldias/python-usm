#Nota: Los archivos de los grupos del 3 al 8 fueron creados por el ayudante Carlos Chesta (http://ayudantiaprograusm.wordpress.com/)

def obtener_equipos(archivo):
	#Nos piden lista, creamos conjunto para despues pasar a lista
	equipos = set()
	#Abrimos y leemos el archivo
	grupo = open(archivo)
	for linea in grupo:
		#Limpiamos y dividimos por "-"
		partido = linea.strip().split("-") #["Espania;1", "Holanda;5"]
		#Necesitamos obtener el nombre de cada equipo, para agregarlo a la lista
		equipos.add(partido[0].split(";")[0])
		equipos.add(partido[1].split(";")[0])

	grupo.close()
	#Y devolvemos una lista con los equipos
	return list(equipos)

#Prueba
print obtener_equipos('Grupo2.txt')

def obtener_clasificados(archivo):
	#Usaremos un diccionario con la estructura nombre_equipo: [puntos, goles]
	puntajes = dict()

	#Primero, obtenemos todos los grupos del archivo
	equipos = obtener_equipos(archivo)
	#Ahora, vamos poblando el diccionario
	for equipo in equipos:
		puntajes[equipo] = [0, 0]

	#Ahora, leemos linea por linea el archivo del grupo, y vemos los partidos (cada linea)
	#Dependiendo del resultado, actualizamos nuestro diccionario de puntajes	
	grupo = open(archivo)
	for partido in grupo:
		equipos = partido.strip().split("-")
		#Separamos ambos equipos
		equipo_1 = equipos[0].split(";") #["Espania","1"]
		equipo_2 = equipos[1].split(";") #["Holanda","5"]

		#Obtenemos lo puntajes actuales
		puntos_1, goles_1 = puntajes[equipo_1[0]]
		puntos_2, goles_2 = puntajes[equipo_2[0]]

		#Cual de los equipos gano?
		if equipo_1[1] > equipo_2[1]: #Gana equipo 1
			#Actualizamos acorde al resultado
			puntos_1 += 3
			goles_1  += int(equipo_1[1])

			puntos_2 += 0
			goles_2  += int(equipo_2[1])
		
		elif equipo_1[1] < equipo_2[1]: #Gana equipo 2
			#Actualizamos acorde al resultado
			puntos_1 += 0
			goles_1  += int(equipo_1[1])

			puntos_2 += 3
			goles_2  += int(equipo_2[1])

		else: #Empate
			#Actualizamos acorde al resultado
			puntos_1 += 1
			goles_1  += int(equipo_1[1])

			puntos_2 += 1
			goles_2  += int(equipo_2[1])

		#Guardamos los puntajes actualizados
		puntajes[equipo_1[0]] = [puntos_1, goles_1]
		puntajes[equipo_2[0]] = [puntos_2, goles_2]
	grupo.close()

	#Para este punto, nuestro diccionario de puntajes tiene los puntos y la cantidad de goles de cada equipo.
	#Para saber el primer y segundo lugar, debemos ordenar. Por conveniencia, transformaremos el diccionario
	#en una lista de tuplas con la estructura (puntos, goles, nombre). Asi, al aplicar sort(), se ordenara
	#primero por el puntaje y despues por la cantidad de goles.

	puntajes_lista = []

	for nombre, [puntos, goles] in puntajes.items():
		puntajes_lista.append( (puntos, goles, nombre) )

	#Ordenamos nuestra lista de tuplas de mayor a menor
	puntajes_lista.sort()
	puntajes_lista.reverse()

	#Solo necesitamos los primeros dos equipos
	return ( puntajes_lista[0][2], puntajes_lista[1][2] )

#Prueba
print obtener_clasificados('Grupo1.txt')
print obtener_clasificados('Grupo2.txt')

def partidos_octavos():
	#Iremos almacenando los grupos clasificados en un diccionario, con la estructura {num_equipo: (equipo1, equipo2)}.
	clasificados = dict()

	#Creamos el archivo donde iran los partidos de octavos de final
	partidos_octavos = open("Partidos_octavos.txt", "w")
	#Obtenemos los grupos clasificados de todos los grupos
	for i in range(1,9):
		clasificados[i] = obtener_clasificados("Grupo" + str(i) + ".txt")
	#Ahora que tenemos todos los datos, podemos comenzar a crear los partidos
	for i in range(1, 8, 2): #[1,3,5,7]
		partidos_octavos.write(clasificados[i][0]+" v/s "+clasificados[i+1][1]+"\n")
		partidos_octavos.write(clasificados[i+1][0]+" v/s "+clasificados[i][1]+"\n")
	
	partidos_octavos.close()
	#La funcion no devuelve nada
	return None

#Prueba
partidos_octavos()

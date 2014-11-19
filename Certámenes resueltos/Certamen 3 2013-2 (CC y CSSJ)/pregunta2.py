def buscar(frase):
	#Primero, separamos la frase en palabras
	palabras_busqueda = frase.lower().split()
	#Creamos un conjunto con los IDs de los libros que contienen, al menos, una de las palabras buscadas
	ids_libros = set()

	#Abrimos el archivo palabras_en_libros.dat, y leemos
	palabras_en_libros = open('palabras_en_libros.dat')
	for linea in palabras_en_libros:
		#Filtramos y obtenemos datos
		palabra, lista_libros = linea.strip().split(":")
		lista_libros = lista_libros.split(",")
		#La palabra esta siendo buscada?
		if palabra in palabras_busqueda:
			#Agregamos toda la lista de libros asociados a esa palabra a nuestro conjunto
			for id_libro in lista_libros:
				ids_libros.add(id_libro)

	palabras_en_libros.close()
	print ids_libros
	#Para este instante, tenemos todos los IDs de libros que tienen, al menos, una de las palabras buscadas.
	#Ahora, para cada libro, debemos obtener la informacion.
	info_libros = []
	
	#Abrimos el archivo libros.dat y leemos
	libros = open('libros.dat')
	for linea in libros:
		#Filtramos y separamos
		id_libro, nombre, autor, anho_pub, estante = linea.strip().split(":")
		#El ID del libro esta en el conjunto?
		if id_libro in ids_libros:
			#Agregamos su info a nuestra lista
			info_libros.append( (nombre, autor, anho_pub, estante) )

	libros.close()
	#Devolvemos la lista
	return info_libros

#Prueba
print buscar('Coronel Aureliano')

def buscar_disponibles(frase):
	#Dejaremos en una lista todos los libros que esten disponibles
	libros_disponibles = []
	#Obtenemos todos los libros que cumplan con la condicion de la funcion anterior
	info_libros = buscar(frase)
	#Recorremos la lista, y desempaquetamos
	for nombre, autor, anho_pub, estante in info_libros:
		#Debemos obtener el ID del libro, para saber si esta o no disponible
		#Para eso usamos el archivo libros.dat
		libros = open('libros.dat')
		for linea in libros:
			datos = linea.strip().split(":")
			#Es este el libro que buscamos?
			if datos[1] == nombre and datos[2] == autor and datos[3] == anho_pub and datos[4] == estante:
				#Si es el libro! Ya tenemos su ID, ahora veamos si esta disponible
				estado = open('estado_libros.dat')
				for linea in estado:
					datos_estado = linea.strip().split(":")
					#Esta disponibiidad corresponde al libro que nos interesa? Esta disponible?
					if datos_estado[0] == datos[0] and datos_estado[1] == "D":
						#El libro esta disponible!
						libros_disponibles.append( (nombre, autor, anho_pub, estante) )
				estado.close()
		libros.close()

	#Ahora, devolvamos los libros disponibles
	return libros_disponibles

#Prueba
print buscar_disponibles('Coronel Aureliano')

def reservar_libro(id_libro):
	#Primero: Creamos nuestro archivo temporal
	temp = open('temp.dat', 'w')
	#Abrimos el archivo estado_libros.dat
	estado_libros = open('estado_libros.dat')
	#Leemos el archivo de estado de libros
	for linea in estado_libros:
		libro, estado = linea.strip().split(":")
		#Es este el libro a modificar:
		if int(libro) == id_libro:
			#Modiicamos su estado
			temp.write(libro+":P\n")
		else:
			#Copiamos tal cual
			temp.write(linea)
	estado_libros.close()
	temp.close()

	#Ahora, pasamos los contenidos de temp a estado_libros.dat
	temp = open('temp.dat')
	estado_libros = open('estado_libros.dat', 'w')
	for linea in temp:
		estado_libros.write(linea)
	estado_libros.close()
	temp.close()
	#Listo! Hemos terminado.

#Prueba
reservar_libro(302)
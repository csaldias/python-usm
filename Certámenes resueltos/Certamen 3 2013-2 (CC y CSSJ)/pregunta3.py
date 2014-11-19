from random import choice

def eleccion_aleatoria(archivo):
	#Nuestra lista donde iran todos los paises del grupo
	paises_grupo = []
	#Primero, abrimos el archivo del grupo y leemos
	grupo = open(archivo)
	for linea in grupo:
		#Filtramos y separamos
		pais = tuple( linea.strip().split(":") )
		#Agregamos el pais a nuestra lista
		paises_grupo.append(pais)
	grupo.close()

	#Devolvemos un pais aleatorio
	return choice(paises_grupo)

#Prueba
print eleccion_aleatoria('bombo2.txt')

def sorteo_grupo(grupo):
	#Mantendremos una lista con las confederaciones contenidas en el grupo...
	confederaciones_grupo = []
	#Los paises que compondran el grupo...
	paises_grupo = []
	#Y los bombos que aun no han sido utilizados.
	grupos_sin_elegir = [2,3,4]

	#Partimos eligiendo un equipo del Bombo 1.
	pais, confederacion = eleccion_aleatoria('bombo1.txt')
	#Lo agregamos directamente al grupo
	paises_grupo.append(pais)
	confederaciones_grupo.append(confederacion)
	
	#Ahora, nos concentramos en los bombos que quedan.
	for i in range(len(grupos_sin_elegir)):
		#Elegimos un bombo al azar de los tres restantes
		num_bombo = choice(grupos_sin_elegir)
		#Elegimos un equipo al azar de este bombo
		pais, confederacion = eleccion_aleatoria('bombo'+str(num_bombo)+'.txt')
		#Como es imposible que un pais este en mas de un bombo, chequeamos que la confederacion de este pais no este en el grupo.
		#Si la confederacion ya esta en el grupo, sequimos eligiendo al azar hasta que la confederacion no este en el grupo.
		while confederacion in confederaciones_grupo:
			pais, confederacion = eleccion_aleatoria('bombo'+str(num_bombo)+'.txt')
			print confederacion
		#Para este punto, la condicion de mas arriba se cumple. Agregamos el pais al grupo
		paises_grupo.append(pais)
		confederaciones_grupo.append(confederacion)
		#Quitamos la tombola de la lista, porque ya la utilizamos.
		grupos_sin_elegir.remove(num_bombo)
	#Ahora, armammos la tupla y la devolvemos
	return ( grupo, paises_grupo )

#Prueba
print sorteo_grupo('Grupo2')

def sorteo_mundial(archivo):
	#Primero, creamos el archivo
	grupos = open(archivo, 'w')
	#Creamos una lista donde iremos guardando los paises que van saliendo.
	paises_elegidos = []

	#Vamos armando los grupos!
	for letra_grupo in ["A","B","C","D","E","F","G","H"]:
		#Asumimos que los paises del grupo que se forma no han salido antes, hasta que se compruebe lo contrario
		grupo_valido = False
		#Repetimos hasta obtener un grupo valido
		while not grupo_valido:
			#Creamos un grupo al azar
			_, paises_grupo = sorteo_grupo('Grupo'+letra_grupo)
			#Chequeamos si acaso algun pais ya fue elegido antes
			for pais in paises_grupo:
				if  pais in paises_elegidos:
					#Un pais ya fue elegido! Este grupo no sirve :(
					grupo_valido = False
					#No vale la pena seguir revisando
					break
			#Si llegamos a este punto, el grupo es valido.
			grupo_valido = True

		#Para este punto, obtenemos un grupo valido. Lo agregamos a la lista y al archivo
		for pais in paises_grupo:
			paises_elegidos.append(pais)

		paises_grupo_str = ":".join(paises_grupo)
		grupos.write("Grupo"+letra_grupo+":"+paises_grupo_str+"\n")

	grupos.close()
	#No devolvemos nada.

#Prueba
sorteo_mundial('grupos.txt')
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
	#Por hacer


def sorteo_mundial(archivo):
	#Por hacer
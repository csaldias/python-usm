#Los datos de ejemplo del problema.
mapa = {
	'A': {'B', 'C'},
	'B': {'A', 'D', 'E', 'G'},
	'C': {'A', 'D'},
	'D': {'B', 'C', 'E', 'G', 'F'},
	'E': {'B', 'D', 'G'},
	'F': {'D'},
	'G': {'E', 'B', 'D'},
	}
 
#Pregunta a)
def son_vecinas(mapa, p, q):
    #Basta con comprobar si q se encuentra entre los vecinos de p para saber si acaso
    #son vecinos entre si. En este caso, comprobar el caso inverso esta de mas.
    if q in mapa[p]:
    	return True
    else:
    	return False

#Pregunta b)
def tienen_vecino_en_comun(mapa, p, q):
    #Obtengamos los conjuntos de vecinos de p y q
    vecinos_p = mapa[p]
    vecinos_q = mapa[q]
    #Para saber si acaso tienen un vecino en comun, intersectamos los conjuntos
    vecinos_en_comun = vecinos_p & vecinos_q
    #Si la interseccion no es vacia, significa que existe al menos una ciudad
    #en comun
    if len(vecinos_en_comun) != 0:
        return True
    else:
        return False

#Pregunta c)
def existe_ruta(mapa, ruta):
	ruta_valida = True
	#Iteramos sobre la ruta, "excluyendo" el ultimo elemento (el por que de esto
	#esta mas abajo)
	for i in range(len(ruta)-1):
        #Iremos asociando los elementos de la ruta de a pares. En el ejemplo del
        #certamen, tendriamos: E-D, D-G, G-B, B-A. Esta es la razon de por que no
        #iteramos hasta el ultimo elemento.
		ciudad_a = ruta[i]
		ciudad_b = ruta[i+1]
		#Son estas dos ciudades vecinas?
		#Si algun par de ciudades no es vecina, entonces la ruta deja de ser valida.
		if not son_vecinas(mapa, ciudad_a, ciudad_b):
			ruta_valida = False
	return ruta_valida

#Prueba
print son_vecinas(mapa, 'A', 'B')
print son_vecinas(mapa, 'C', 'G')

print tienen_vecino_en_comun(mapa, 'C', 'E')
print tienen_vecino_en_comun(mapa, 'A', 'F')

print existe_ruta(mapa, ['E', 'D', 'G', 'B', 'A'])
print existe_ruta(mapa, ['A', 'B', 'C', 'D', 'E'])
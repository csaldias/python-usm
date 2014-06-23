def son_anagramas(p1, p2):
	#Copiamos p1, para iterar sobre ella
	p1_iter = p1
	#Pasamos nuestras 2 palabras a listas
	p1_lista = list(p1)
	p2_lista = list(p2)

	#Iteramos sobre nuestra copia
	for letra in p1_iter:
		#Aqui viene la magia (?!)
		#Si una letra de la primera palabra esta tambien en la
		#segunda palabra, la eliminamos de ambas.
		if (letra in p1_lista) and (letra in p2_lista):
			p1_lista.remove(letra)
			p2_lista.remove(letra)
	#Si las palabras son anagramas, ambas listas deberian quedar
	#vacias. Si no, es porque no son anagramas.
	if p1_lista and p2_lista:
		return False
	else:
		return True

#Prueba
print son_anagramas('torpes', 'postre')
print son_anagramas('aparta', 'raptar')

def es_panvocalica(palabra):
	#Nuestra lista de vocales
	vocales = 'aeiou'
	#Asumimos que la palabra es panvocalica hasta que se demuestre
	#lo contrario.
	es_panvocalica = True
	for vocal in vocales:
		#Si alguna vocal no esta en la palabra...
		if vocal not in palabra:
			#Es porque la palabra no es panvocalica.
			es_panvocalica = False
	return es_panvocalica

#Prueba
print es_panvocalica('educativo')
print es_panvocalica('pedagogico')

def cuenta_panvocalicas(oracion):
	#Separamos las palabras
	palabras = oracion.split()
	#Llevamos la cuenta de palabras panvocalicas en la oracion
	cuenta_panvocalicas = 0
	for palabra in palabras:
		#Si la palabra es panvocalica...
		if es_panvocalica(palabra):
			#Actualizamos la cuenta
			cuenta_panvocalicas += 1
	return cuenta_panvocalicas

#Prueba
print cuenta_panvocalicas('el abuelito mordisquea el aceituno con contundencia')
print cuenta_panvocalicas('la contertulia estudiosa va a casa')
print cuenta_panvocalicas('los hipopotamos bailan al amanecer')

def tiene_letras_en_orden(palabra):
	#Pasamos la palabra a lista
	lista_palabra = list(palabra)
	lista_palabra_ordenada = list(palabra)
	#Ordenamos una de las dos
	lista_palabra_ordenada.sort()
	#Si son iguales, es porque la palabra tiene sus letras en orden alfabetico
	if lista_palabra == lista_palabra_ordenada:
		return True
	else:
		return False

#Prueba
print tiene_letras_en_orden('himnos')
print tiene_letras_en_orden('abenuz')
print tiene_letras_en_orden('zapato')

def tiene_letras_dos_veces(palabra):
	#Creamos un diccionario para llevar la cuenta
	frec_letra = {}
	#Iteramos nuestra palabra
	for letra in palabra:
		if letra in frec_letra:
			frec_letra[letra] += 1
		else:
			frec_letra[letra] = 1
	
	#Para este entonces, frec_letra tiene la cantidad
	#de veces que aparece cada letra de la palabra.
	#Para que la palabra cumpla con la condicion, cada
	#letra debe aparecer exactamente 2 veces.
	for frec in frec_letra.values():
		#Si pilla alguna letra que no este 2 veces en
		#la palabra, no tiene caso seguir y devolvemos
		#false.
		if frec != 2:
			return False
	#Si no pillamos alguna letra que no este 2 veces
	#en la palabra, estamos bien.
	return True

#Prueba
print tiene_letras_dos_veces('aristocraticos')
print tiene_letras_dos_veces('quisquilloso')
print tiene_letras_dos_veces('aristocracia')

def palabras_repetidas(oracion):
	#Creamos un diccionario para llevar la cuenta
	frec_palabras = {}
	#Lista de palabras repetidas mas de una vez
	palabras_repetidas = []
	#iteramos sobre nuestra oracion
	for palabra in oracion.lower().split():
		if palabra in frec_palabras:
			frec_palabras[palabra] += 1
		else:
			frec_palabras[palabra] = 1
	for palabra in frec_palabras:
		#Si alguna palabra sale mas de una vez en la oracion...
		if frec_palabras[palabra] > 1:
			#La agregamos a nuestra lista
			palabras_repetidas.append(palabra)
	return palabras_repetidas

#Prueba
print palabras_repetidas('El partido termino cero a cero')
print palabras_repetidas('El sobre esta sobre el mueble')
print palabras_repetidas('Ay, ahi no hay pan')

def es_pangrama(texto):
	#La palabra es pangrama hasta que se pruebe lo contrario
	es_pangrama = True
	#Me da lata escribir todas las letras de la a a la z, asi que
	#usaremos el metodo ASCII. Este sistema asocia a cada caracter
	#un numero. En este caso, 97 para la a y 122 para la z. Entre
	#el 97 y el 122 viven todas las letras de la a la z, y con
	#chr(cod) obtengo la letra asociada a un cierto codigo.
	for codigo in range(97,123):
		#Si alguna letra del abecedario (gringo) no esta en la palabra...
		if chr(codigo) not in texto.lower():
			#Es porquq no es pangrama.
			es_pangrama = False
	return es_pangrama

#Prueba
print es_pangrama('Sylvia wagt quick den Jux bei Pforzheim.')
print es_pangrama('Cada vez que trabajo, Felix me paga un whisky.')
print es_pangrama('Cada vez que trabajo, Luis me invita a una cerveza.')
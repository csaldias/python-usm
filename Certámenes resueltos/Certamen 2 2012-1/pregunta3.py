#Los datos del problema.
inventario = {
	'huevos': 12,		# unidades
	'leche': 500,		# ml
	'papas': 3,			# unidades
	'margarina': 200,	# gr
	'azucar': 200,		# gr
	'sal': 50,			# gr
	'queso': 4,			# rebandas
	'pan': 12,			# rebanadas
	'te': 5,			# bolsas
	# ...
}

recetas = {
	'omelette': [(2, 'huevos'), (15, 'margarina'),
				 (1, 'sal'), (10, 'leche')],
	'omelette con queso': [(2, 'huevos'), (10, 'margarina'),
						   (2, 'queso'), (10, 'leche')],
	'pan con queso': [(2, 'pan'), (5, 'margarina'), (1, 'queso')],
	'te con leche': [(1, 'te'), (10, 'leche'), (10, 'azucar')],
	'vaso de leche': [(500, 'leche')],
	# ...
}

#Pregunta a)
def ingredientes(num_porciones, plato):
	plato_porciones = {}
	#Iteramos sobre los ingredientes del plato a preparar
	for cantidad, ingrediente in recetas[plato]:
		#Multiplicamos la cantidad del ingrediente por el numero
		#de porciones, y lo guardamos todo en el diccionario
		plato_porciones[ingrediente] = num_porciones * cantidad
	return plato_porciones

#Pregunta b)
def numero_de_porciones(plato, inv):
	max_porciones = 999999999
	for cantidad, ingrediente in recetas[plato]:
		porciones = inventario[ingrediente] / cantidad
		if porciones < max_porciones:
			max_porciones = porciones
	return max_porciones

#Pregunta c)
def cocinar_juntos(pedido, inv):
	#Iteramos sobre el pedido
	for numero_porciones, plato in pedido:
		#Si el numero maximo de porciones de un plato esta bajo la cantidad pedida...
		if numero_de_porciones(plato, inv) < num_porciones:
			#Devolvemos False
			return False
	#Caso contrario, devolvemos True
	return True

#Prueba
print ingredientes(2, 'omelette')
print ingredientes(3, 'te con leche')

print numero_de_porciones('omelette', inventario)
print numero_de_porciones('pan con queso', inventario)

print cocinar_juntos([(2, 'omelette'), (2, 'te con leche')], inventario)
print  cocinar_juntos([(1, 'omelette con queso'), (1, 'pan con queso'), (500, 'vaso de leche')], inventario)

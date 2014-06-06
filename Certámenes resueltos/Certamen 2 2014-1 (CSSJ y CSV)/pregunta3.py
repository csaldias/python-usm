#Datos del problema.
competencia = {
	'pista': {'v100mt','v400mt','v800mt','v3000mt','d100mt','d400mt'},
	'campo': {'vbala','vdisco','vlargo','dbala'}
}

puntaje = {
	'lugar 1': 12, #Medalla
	'lugar 2': 9,  #Medalla
	'lugar 3': 7,  #Medalla
	'lugar 4': 5,
	'lugar 5': 4,
	'lugar 6': 3,
	'lugar 7': 2,
	'lugar 8': 1
}

resultado = {
	'usm'  : [('mrios','v400mt',9), ('nmassu','v3000mt',12), ('jrojas','vdisco',12)],
	'usach': [('jramos','d400mt',5), ('lsoto','d400mt',9), ('mruiz','v800mt',7)],
	'uc'   : [('mhard','v100mt',3), ('msolis','d3000mt',5), ('lrozas','dbala',5)]
}

#Pregunta a)
def participante_prueba(competencia, resultado, prueba):
	nombres = []
	#Iteramos sobre los resultados
	for lista_por_u in resultado.values():
		#Vamos desempaquetando...
		for nombre_competidor, prueba_competidor, ptje in lista_por_u:
			#Si la prueba del competidor esta dentro del grupo de pruebas solicitado...
			if prueba_competidor in competencia[prueba]:
				#Guardamos su nombre
				nombres.append(nombre_competidor)
	
	return nombres

#Pregunta b)
def mayor_cantidad(resultado, puntaje):
	#Algunas variables auxiliares
	mayor_medallas = -1
	mayor_u = ""
	#Iteramos sobre las llaves y valores de resultado
	for universidad, competidores in resultado.items():
		#Var auxiliar
		cant_medallas = 0
		#Iteramos sobre la lista de competidores
		for nombre_competidor, prueba_competidor, ptje in competidores:
			#Si el competidor obtuvo alguna medalla...
			if ptje == puntaje['lugar 1'] or ptje == puntaje['lugar 2'] or ptje == puntaje['lugar 3']:
				#Aumentamos la cuenta
				cant_medallas += 1
		#Si la cuenta de medallas es mayor que la maxima...
		if cant_medallas >= mayor_medallas:
			#Actualizamos valores
			mayor_medallas = cant_medallas
			mayor_u = universidad

	return mayor_u

#Pregunta c)
def prueba_sin_medallas(resultado, puntaje):
	pruebas_no_medalla = []
	#Iteramos sobre los valores de resultado
	for lista_por_u in resultado.values():
		#Desempaquetamos
		for nombre_competidor, prueba_competidor, ptje in lista_por_u:
			#Si la prueba no tiene medalla...
			if not (ptje == puntaje['lugar 1'] or ptje == puntaje['lugar 2'] or ptje == puntaje['lugar 3']):
				#La agregamos.
				pruebas_no_medalla.append(prueba_competidor)
			#Debemos filtrar los "colados", las pruebas que se agregan a la lista teniendo una medalla
			elif (ptje == puntaje['lugar 1'] or ptje == puntaje['lugar 2'] or ptje == puntaje['lugar 3']) and prueba_competidor in pruebas_no_medalla:
				pruebas_no_medalla.remove(prueba_competidor)
	return pruebas_no_medalla

#Prueba
print participante_prueba(competencia, resultado, 'campo')

print mayor_cantidad(resultado, puntaje)

print prueba_sin_medallas(resultado, puntaje)
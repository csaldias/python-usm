#Datos de ejemplo del problema.
alumnos = [
		('201021056-k', 'fis100', 60), ('201304119-3', 'mat021', 85),
		('201341039-4', 'mat021', 49), ('201304119-3', 'iwi131', 98),
		('201341039-4', 'qui010', 60), ('201021056-k', 'mat021', 68),
		('201341039-4', 'fis100', 56), ('201021056-k', 'qui010', 70),
		('201021056-k', 'elo270', 82), ('201304119-3', 'fis100', 80)
		]

#Pregunta a)
def promedio_asignatura(asignatura,alumnos):
	notas = []
	#Iteramos sobre la lista de alumnos
	for _, codigo_asignatura, nota in alumnos:
		#Si la asignatura corresponde a la que buscamos...
		if codigo_asignatura == asignatura:
			#Agregamos la nota del alumno a nuestra lista
			notas.append(nota)
	#Calculamos el promedio
	promedio = sum(notas)/len(notas)
	#Devolvemos el promedio redondeado
	return round(promedio)

#Pregunta b)
def resumen_academico_semestral(rol,alumnos):
	resumen_academico = {}
	#Iteramos sobre la lista de alumnos
	for rol_alumno, codigo_asignatura, nota in alumnos:
		#Si el rol es igual al que buscamos...
		if rol_alumno == rol:
			#Agregamos su informacion
			resumen_academico[codigo_asignatura]=nota
	return resumen_academico

#Pregunta c)
def resumen_asignaturas(alumnos,ramos):
	resumen = []
	#Iteramos sobre la lista de ramos
	for ramo in ramos:
		#Obtenemos el promedio del ramo, y lo empaquetamos
		resumen.append((ramo, promedio_asignatura(ramo,alumnos)))
	return resumen

#Prueba
print promedio_asignatura('mat021',alumnos)
print resumen_academico_semestral('201021056-k',alumnos)
print resumen_asignaturas(alumnos, ["iwi131","fis100","mat021"])
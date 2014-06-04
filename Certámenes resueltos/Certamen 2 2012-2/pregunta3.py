#Los datos de ejemplo del problema.
datos1 = {'nombre' : 'Oliver',
		 'apellido' : 'Atton',
		 'edad' : 31,
		 'peso' : 87.0,
		 'estatura' : 1.8,
		 'presion arterial': 90.,
		 'ritmo cardiaco' : 60.
		 }

datos2 = {'nombre' : 'Jimmy',
		 'apellido' : 'Page',
		 'edad' : 55,
		 'peso' : 100.0,
		 'estatura' : 1.75,
		 'presion arterial': 90.,
		 'ritmo cardiaco' : 60.
		 }

pacientes = [('15000111-7', datos1), ('15111222-3', datos2)]

#Pregunta a)
def nuevo_paciente(ficha):
	#Si la ficha no existe en pacientes...
	if ficha not in pacientes:
		#La ingresamos.
		pacientes.append(ficha)
		return "Ingresado"
	else:
		#Si no, avisamos que ya exsite.
		return "Ya existe"

#Pregunta b)
def modificar_paciente(rut, clave, valor):
	#Como no podemos modificar un objeto que estemos utilizando, debemos crear
	#una copia de pacientes para poder iterarla y modificar la "original"
	pacientes_itera = pacientes
	#Iteramos y desempaquetamos
	for rut_paciente, datos_paciente in pacientes_itera:
		#Si los ruts coinciden...
		if rut_paciente == rut:
			#Hacemos la modificacion.
			#Eliminamos el registro anterior de paciente...
			pacientes.remove((rut_paciente, datos_paciente))
			#Actualizamos los datos...
			datos_paciente[clave]=valor
			#Y guardamos el nuevo registro.
			pacientes.append((rut_paciente, datos_paciente))
			return "Actualizado"
	#Si llega aca, es porque el rut no existe en pacientes.
	return "No existe"

#Pregunta c)
def filtrar(p):
	datos_filtrados = []
	#Primero iteramos sobre los pacientes.
	for rut, datos in pacientes:
		#Creamos una lista temporal para ir agregando datos
		datos_temp = []
		#iteramos sobre la lista de filtros
		for filtro in p:
			#Agregamos a datos_temp los datos pedidos
			datos_temp.append(datos[filtro])
		#Ya teniendo todos los datos, pasamos todo a tupla y
		#agregamos a nuestra lista.
		datos_filtrados.append(tuple(datos_temp))
	return datos_filtrados	

#Prueba
ficha = ('14999888-6', datos1)
print nuevo_paciente(ficha)
print nuevo_paciente(ficha)

print modificar_paciente('15000111-7', 'edad', 35)
print modificar_paciente('12002299-6', 'edad', 43)

pacientes = [('15000111-7', datos1), ('15111222-3', datos2) ]
p = ('edad', 'peso')
print filtrar(p)
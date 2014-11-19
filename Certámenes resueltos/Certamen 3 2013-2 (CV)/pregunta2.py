def zonas(area, archivo):
	#Piden lista, creamos lista
	zonas_mayor_area = []

	#Abrimos el arhivo de zonas y leemos
	zonas = open(archivo)
	for zona in zonas:
		#Obtenemos los datos de la zona
		datos_zona = zona.strip().split(":")
		#Si el area de la zona es mayor a la deseada...
		if int(datos_zona[2]) > area:
			#Agregamos la zona a nuestra lista.
			zonas_mayor_area.append(datos_zona[0])

	zonas.close()
	#Devolvemos la lista
	return zonas_mayor_area

#Prueba
print zonas(7, 'zonas.txt')

def ley_promedio(zonas, archivo):
	#Definimos variables que vamos a usar para sacar el promedio
	suma_ley_cobre = 0.0
	cantidad_subzonas = 0
	#Abrimos el archivo de subzonas y leemos
	subzonas = open(archivo)
	for subzona in subzonas:
		datos_subzona = subzona.strip().split(":")
		#Si la zona a la que corresponde esta subzona esta en la lista de zonas...
		if datos_subzona[0] in zonas:
			#Actualizamos variables
			suma_ley_cobre += float(datos_subzona[2])
			cantidad_subzonas += 1

	subzonas.close()
	#Devolvemos el promedio
	return suma_ley_cobre / cantidad_subzonas

#Prueba
print ley_promedio(['z1','z2'], 'subzonas.txt')

def mejor_zona(Estado, archivo1, archivo2):
	#Definimos el mayor promedio de ley de todas las subzonas de una zona
	mayor_promedio_ley = 0.0

	#Abrimos el archivo de zonas y leemos
	zonas = open(archivo1)
	for zona in zonas:
		datos_zona = zona.strip().split(":")
		#Si el estado de esta zona corresponde al deseado...
		if datos_zona[1] == Estado.lower():
			#Calculamos el promedio de todas sus subzonas
			promedio_subzonas = ley_promedio([ datos_zona[0] ], archivo2)
			#Si el promedio de las subzonas de esta zona es el mayor...
			if promedio_subzonas > mayor_promedio_ley:
				#Actualizamos valores
				mayor_promedio_ley = promedio_subzonas
				mayor_zona = datos_zona[0]

	zonas.close()
	#Devolvemos los valores en forma de tupla
	return ( mayor_zona, mayor_promedio_ley )

#Prueba
print mejor_zona('Programado','zonas.txt','subzonas.txt')
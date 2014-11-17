def crypto_monedas(archivo):
	#Nos piden conjunto, hacemos un conjunto
	cryptomonedas = set()

	#Abrimos el archivo
	datos_conversion = open(archivo)
	#Leemos el archivo, linea por linea
	for linea in datos_conversion:
		#Limpiamos la linea (strip) y la dividimos por el ":" (split)
		datos = linea.strip().split(":") #[nombre, valor_coversion]
		#Agregamos el nombre de la cryptomoneda, que es lo que nos interesa
		cryptomonedas.add(datos[0])

	#Devolvemos el conjunto
	return cryptomonedas

#Para probar
print crypto_monedas('conversiones.txt')

def crypto_monedas_alumno(rol, archivo):
	#Nos piden conjunto, hacemos un conjunto
	monedas_pago = set()

	#Abrimos el archivo
	datos_pagos = open(archivo)
	#Vamos linea por linea en el archivo
	for linea in datos_pagos:
		#Limpiamos la linea (strip) y la dividimos por el ":" (split)
		datos_alumno = linea.strip().split(":") #[rol, moneda, monto]
		#Si el rol corresponde al buscado...
		if datos_alumno[0] == rol:
			#Agregamos la moneda utilizada a nuestro conjunto
			monedas_pago.add(datos_alumno[1])

	#Devolvemos el diccionario
	return monedas_pago

#Para probar
print crypto_monedas_alumno('201573021-4','pagos.txt')
print crypto_monedas_alumno('201533092-1','pagos.txt')

def deuda_alumno(rol, archivo1, archivo2):
	#Valor del arancel, en BTC
	valor_arancel = 10.0
	#Pagos realizados por el alumno, en BTC
	pago_alumno = 0.0

	#Primero: abrimos pagos.txt y obtenemos el pago del alumno y bajo que moneda
	#Procedemos igual que antes...
	datos_pagos = open(archivo2)
	for linea in datos_pagos:
		datos_alumno = linea.strip().split(":") #[rol, moneda, monto]
		#Si este es el rol del alumno buscado...
		if datos_alumno[0] == rol:
			#Si el pago se hizo en bitcoin, lo sumamos
			if datos_alumno[1] == 'bitcoin':
				pago_alumno += float(datos_alumno[2])
			else: #Si no, tendremos que convertirlo a BTC.
				#Leemos el arhivo conversiones.txt
				datos_conversion = open(archivo1)
				for linea in datos_conversion:
					conversion = linea.strip().split(":") #[moneda, valor_conversion]
					#Si el dato de conversion corresponde a la moneda...
					if conversion[0] == datos_alumno[1]:
						#Convertimos el valor a BTC y sumamos.
						pago_alumno += float(conversion[1])*float(datos_alumno[2])

	#Calculamos la deuda del alumno
	deuda = valor_arancel - pago_alumno
	#Y devolvemos
	return deuda

#Para probar
print deuda_alumno('201573101-8', 'conversiones.txt', 'pagos.txt')
print deuda_alumno('201533092-1', 'conversiones.txt', 'pagos.txt')

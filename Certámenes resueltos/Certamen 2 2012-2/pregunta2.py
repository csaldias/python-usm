#Datos de ejemplo del problema.
monedas = { 'US' : ('Dolares Americanos', 500),
			'EUR' : ('Euros', 600),
			'L' : ('Libras', 700),
			'CH' : ('Pesos Chilenos', 1)
		}

venta_diaria = [('US', 50), ('L', 200), ('EUR', 300), ('L', 100), ('CH', 21000), ('US', 150), ('EUR', 100)]

#Pregunta a)
def por_moneda(monedas, venta_diaria):
	total_vendido = {}
	#Iteramos sobre el diccionario monedas
	for codigo_moneda, datos in monedas.items():
		#Desempaquetamos la tupla de datos
		descripcion_moneda, valor_cambio = datos
		for codigo_venta, monto in venta_diaria:
			#Si el codigo de la moneda de la venta es igual al codigo de la moneda analizada...
			if codigo_moneda == codigo_venta:
				#Si la moneda no esta en nuestro diccionario...
				if descripcion_moneda not in total_vendido:
					#La agregamos
					total_vendido[descripcion_moneda] = monto
				else:
					#Como esta, actualizamos el valor
					total_vendido[descripcion_moneda] += monto
	return total_vendido

#Pregunta b)
def total_venta_diaria(monedas, venta_diaria):
	ventas_ch = 0
	#Obtenemos la venta del dia, utilizando la funcion anterior
	ventas_dia = por_moneda(monedas, venta_diaria)
	#Recorremos este diccionario
	for descripcion_moneda_venta, monto_venta in ventas_dia.items():
		#Recorremos los valores del diccionario moneda
		for descripcion_moneda, tasa_cambio in monedas.values():
			#Si la descripcion de la moneda de la venta es la moneda que estamos analizando
			#en esta iteracion...
			if descripcion_moneda_venta == descripcion_moneda:
				#Usamos la tasa de cambio para obtener el equivalente
				#en pesos chilenos
				ventas_ch += monto_venta * tasa_cambio
	return ventas_ch

#Pregunta c)
def convertir(venta_diaria, monedas, m):
	valores_diarios = []
	#Obtenemos la tasa de cambio de la moneda pedida
	tasa_cambio_m = monedas[m][1]
	#Iteramos sobre venta_diaria
	for codigo_moneda_venta, monto in venta_diaria:
		#Iteramos sobre los valores del diccinario monedas
		for codigo_moneda, (_, tasa_cambio_ch) in monedas.items():
			#Si la moneda siendo analizada esta en venta_diaria...
			if codigo_moneda == codigo_moneda_venta:
				#Agregamos el monto de la venta a nuestra lista.
				#Observar el flujo: moneda1 -> peso_ch -> moneda_m
				valores_diarios.append((monto * tasa_cambio_ch) / tasa_cambio_m)
	return valores_diarios

#Prueba
print por_moneda(monedas, venta_diaria)
print total_venta_diaria(monedas, venta_diaria)
print convertir(venta_diaria, monedas, 'EUR')
print convertir(venta_diaria, monedas, 'CH')
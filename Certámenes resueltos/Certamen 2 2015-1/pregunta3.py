#Datos de la Pregunta 3
#{id_cliente:[(serv1, serv2, serv3), saldo_mensual, [canalprem1, canalprem2, ...], deuda]}
clientes = {
	23:  [('telefonia', 'cable', 'internet'), 23000, ['GameKidTV'], False],
	66:  [('internet', 'telefonia', 'cable'), 34000, ['WolfSports', 'ZDFPremium'], True],
	120: [('cable', 'internet'), 30000, ['HVOPrem'], True]
	# ...
}

#[(id_cliente, id_tecnico, fecha_visita)]
visitas_tecnicas = [
	(23, 65, '30-03-2015'),
	(66, 65, '31-03-2015'),
	(120, 33, '28-03-2015')
	# ...
]

#{(id_tecnico, nombre)}
tecnicos = {
	(65, 'Guy Cable'),
	(66, 'Dexter Morgan')
	# ...
}

#Punto a)
def monto_total_deuda(clientes):
	#Guardamos el monto total adeudado y el ID del cliente con mayor deuda
	monto_total_adeudado = 0
	mayor_monto_adeudado = -1
	cliente_mas_deuda = 0
	#Recorremos los clientes
	for id_cliente, (servicios, saldo_mensual, canales_premium, es_deudor) in clientes.items():
		#Si el cliente es deudor...
		if es_deudor:
			#Sumamos su deuda al total
			monto_total_adeudado += saldo_mensual
			#Su deuda es la mas grande?
			if saldo_mensual >= mayor_monto_adeudado:
				#Actualizamos el id del cliente con mayor deuda
				cliente_mas_deuda = id_cliente
				mayor_monto_adeudado = saldo_mensual
	#Dejamos iterar, para que obtenga el monto total de deuda y el cliente con mayor deuda
	#Cuando terminamos, devolvemos en formato tupla
	return (monto_total_adeudado, cliente_mas_deuda)

#Probando, probando...
print monto_total_deuda(clientes)

#Punto b)
def promocion(clientes):
	#Como no podemos modificar un diccionario mientras lo recorremos,
	#creamos un diccionario vacio donde dejamos las modificaciones
	clientes_promo = dict()
	#Recorremos los clientes
	for id_cliente, (servicios, saldo_mensual, canales_premium, es_deudor) in clientes.items():
		#Si el cliente no tiene deuda y tiene contratado los tres servicios...
		if not es_deudor and len(servicios) == 3:
			#Si el cliente no tiene el canal 'GameKidTV', se lo damos
			if 'GameKidTV' not in canales_premium:
				canales_premium.append('GameKidTV')
			#Si ya lo tiene, le descontamos 500 de su saldo mensual
			else:
				saldo_mensual -= 500
		#Guardamos los cambios en nuestra lista secundaria
		clientes_promo[id_cliente] = [servicios, saldo_mensual, canales_premium, es_deudor]
	#Dejamos que itere, para que realice todas las modificaciones necesarias que especifica la promo.
	#Cuando terminamos, devolvemos nuestra nueva lista
	return clientes_promo

#Probando, probando...
print promocion(clientes)

#Punto c)
def premio_tecnico(clientes, visitas_tecnicas, tecnicos):
	#Primero, tenemos que encontrar al tecnico con mas visitas realizadas en el mes de marzo, junto con los clientes que visito.
	#Para eso, creamos un diccionaro con la estructura {id_tecnico: [num_visitas, [cliente1, cliente2, ...]]}
	visitas_por_tecnico = dict()
	#Iteramos en visitas_tecnicas
	for id_cliente, id_tecnico, fecha_visita in visitas_tecnicas:
		#Si la visita fue realizada en el mes de marzo...
		if fecha_visita.split('-')[1] == '03':
			#Si el tecnico ya esta en el diccionario de visitas...
			if id_tecnico in visitas_por_tecnico:
				#Actualizamos su cantidad de visitas y los clientes que visito
				visitas_por_tecnico[id_tecnico][0]+=1
				visitas_por_tecnico[id_tecnico][1].append(id_cliente)
			#Si no esta en el diccionario de visitas...
			else:
				#Lo agregamos
				visitas_por_tecnico[id_tecnico]=[1, [id_cliente]]
	#Lo dejamos iterar, para tener un diccionario con las visitas que realizo cada tecnico en el mes de marzo, junto con los clientes que visito.
	#Ahora, vemos que tecnico realizo la mayor cantidad de visitas, y a que clientes
	mayor_visitas = -1
	id_tecnico_mas_visitas = 0
	clentes_visitados_por_tecnico = []
	#Iteramos nuestro diccionario:
	for id_tecnico, (num_visitas, clientes_visitados) in visitas_por_tecnico.items():
		#Si este tecnico realizo mas visitas que el tecnico anterior...
		if num_visitas >= mayor_visitas:
			#Actualizamos los datos
			mayor_visitas = num_visitas
			id_tecnico_mas_visitas = id_tecnico
			clientes_visitados_por_tecnico = clientes_visitados
	#Dejamos que itere, para obtener el id del tecnico que realizo la mayor cantidad de visitas, junto con los clientes que visito.
	#Ahora, necesitamos conocer el premio de este tecnico. Para eso, necesitamos conocer el saldo mensual y la cantidad de servicios
	#contratados por cada cliente visitado.
	premio_total = 0
	#Iteramos en la lista de clientes
	for id_cliente in clientes_visitados_por_tecnico:
		#Obtenemos los datos del cliente
		servicios, saldo_mensual, canales_premium, deuda = clientes[id_cliente]
		#Calculamos el premio de este cliente
		premio_total += (saldo_mensual*0.01)*len(servicios)
	#Dejamos que itere, y obtenemos el premio del tecnico con mas visitas.
	#Ahora, necesitamos el nombre del tecnico en cuestion.
	nombre_tecnico = ""
	for id_tecnico, nombre in tecnicos:
		#Si este es nuestro tecnico...
		if id_tecnico == id_tecnico_mas_visitas:
			#Guardamos el nombre
			nombre_tecnico = nombre
	#Dejamos iterar, para obtener el nombre de nuestro tecnico.
	#Ahora, devolvemos el nombre del tecnico y su premio en formato tupla
	return (nombre_tecnico, int(premio_total))

#Probando, probando...
print premio_tecnico(clientes, visitas_tecnicas, tecnicos)
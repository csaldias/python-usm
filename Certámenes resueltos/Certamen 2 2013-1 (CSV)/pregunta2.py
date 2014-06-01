#Datos de ejemplo del problema.
clientes = {
	#RUT: [nombre,edad,sucursal,(monto1,monto2,monto3)]
	'16034124-5': ['Fernando Ruiz Diaz', 30,'Vina', (100,200,300)],
	'5436576-2': ['Mike Portnoy',20, 'Quilpue', (100, 100, 50)],
	'3333333-3': ['Slash', 50,'Vina', (500,550,300)],
	'1234567-8': ['Cliff Burton', 35,'Valparaiso', (50,50,100)]
	#...
}

#DETALLE: En el enunciado sale que los valores del diccionario son listas,
#         pero en el diccionario de ejemplo salian como tuplas. Yo modifique
#         el diccionario de ejemplo para que respetara el enunciado (esto es,
#         que los valores del diccionario fueran realmente listas).

#Pregunta a)
def misma_sucursal(rut1, rut2, clientes):
	#Obtenemos la sucursal de ambos clientes
	sucursal_1 = clientes[rut1][2]
	sucursal_2 = clientes[rut2][2]
	#Chequeamos si acaso son iguales
	if sucursal_1 == sucursal_2:
		return True
	else:
		return False

#Pregunta b)
def mayores_que(edad_minima,clientes):
	filtro_clientes = []
	#Como no necesitamos los RUTs de las personas, iteramos sobre
	#los valores del diccionario
	for datos in clientes.values():
		#Obtenemos la edad de la persona
		edad = datos[1]
		#Si su edad es mayor o igual a la edad minima...
		if edad >= edad_minima:
			#Agregamos su nombre a nuestra lista
			filtro_clientes.append(datos[0])
	return filtro_clientes

#Pregunta c)
def es_cliente_vip(rut, monto_compra,clientes):
	#Obtenemos los datos del cliente
	datos = clientes[rut]
	#Obtenemos los montos de sus compras
	montos = datos[3]
	#Si la suma de los montos de sus compras es igual o superior al solicitado...
	if sum(montos) >= monto_compra:
		#Devolvemos verdadero
		return True
	else:
		#En caso contrario, devolvemos falso
		return False

#Prueba
print misma_sucursal('16034124-5','3333333-3',clientes)
print misma_sucursal('5436576-2','3333333-3',clientes)
print mayores_que(50,clientes)
print mayores_que(25,clientes)
print es_cliente_vip('5436576-2',500,clientes)
print es_cliente_vip('3333333-3',500,clientes)
print es_cliente_vip('1234567-8',150,clientes)
#Ojo, el ultimo caso no calza con el enunciado: da False porque la suma de los
#montos es igual el monto minimo, cuando por enunciado deberia dar True.
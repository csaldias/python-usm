#Primero, definimos una funcion auxiliar que nos devuelva el valor decimal de cada numero romano
def decimal(letra):
	if letra == "M":
		return 1000
	elif letra == "D":
		return 500
	elif letra == "C":
		return 100
	elif letra == "L":
		return 50
	elif letra == "X":
		return 10
	elif letra == "V":
		return 5
	elif letra == "I":
		return 1

def romano_a_arabigo(num_romano):
	valor_decimal = 0
	#Iteramos sobre todo el numero
	for i in range(len(num_romano)):
		#Obtenemos la letra actual y la letra siguiente
		letra_actual = num_romano[i]
		if i != len(num_romano)-1: #Si existe una letra siguiente
			letra_siguiente = num_romano[i+1]
		else: #Si la letra actual es la ultima del numero romano
			letra_siguiente = letra_actual
		#Las condiciones:
		#Si una letra esta seguida inmediatamente por una de igual o menor valor...
		if decimal(letra_actual) >= decimal(letra_siguiente):
			#Su valor se suma al total acumulado
			valor_decimal += decimal(letra_actual)
		#Si una letra esta seguida inmediatamente por una de mayor valor...
		elif decimal(letra_actual) < decimal(letra_siguiente):
			#Su valor se sustrae del total acumulado
			valor_decimal -= decimal(letra_actual)
	return valor_decimal

#Ahora, probemos la funcion:
print romano_a_arabigo('MCMXIV')
print romano_a_arabigo('XIV')
print romano_a_arabigo('X')
print romano_a_arabigo('IV')
print romano_a_arabigo('DLIV')
print romano_a_arabigo('CCCIII')

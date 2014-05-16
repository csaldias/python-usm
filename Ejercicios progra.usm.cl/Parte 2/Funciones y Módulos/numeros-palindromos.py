def invertir_digitos(num):
	#Pasamos el numero a string.
	num_string = str(num)
	num_inverso = ""
	#Vemos su largo
	largo = len(num_string)
	#Ahora recorremos el string del numero "de atras hacia adelante"
	for i in range(largo-1,-1,-1):
		num_inverso += num_string[i]
	#Y devolvemos el numero invertido
	return int(num_inverso)

#Ahora usamos esta funcion para ver si un numero es palindromo.
#Ej:
#	12321 es palindromo: si lo invierto sigue siendo el mismo numero.
#	12345 no es palindromo: cuando lo invierto se convierte en 54321, que claramente no es el mismo numero.

numero = int(raw_input("Ingrese n: "))
if numero == invertir_digitos(numero):
	print "Es palindromo"
else:
	print "No es palindromo"
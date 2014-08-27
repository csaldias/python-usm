#Primero, pedimos el numero
n = int(raw_input("Ingrese num: "))

#Ahora, generamos las primeras n potencias de dos
#Las potencias van desde 2^0 hasta 2^n
for i in range(n+1):
	print 2**i, #La coma al final hace que el print
				#no pase a la linea de abajo, imprimiendo
				#todo hacia el lado.
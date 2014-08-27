num = int(raw_input("Ingrese numero: "))

#Probamos todos los numeros entre 1 y el numero
#en busca de sus divisores
for i in range(1,num+1):
	if num % i == 0: #Si el resto de la division es cero...
		print i, #Imprime el divisor
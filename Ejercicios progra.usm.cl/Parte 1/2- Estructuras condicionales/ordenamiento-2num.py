#Pedimos los numeros
num_1 = int(raw_input("ingrese numero: "))
num_2 = int(raw_input("ingrese numero: "))

#Y los ordenamos
if num_1 >= num_2:
	print str(num_2)+" "+str(num_1)
else:
	print str(num_1)+" "+str(num_2)
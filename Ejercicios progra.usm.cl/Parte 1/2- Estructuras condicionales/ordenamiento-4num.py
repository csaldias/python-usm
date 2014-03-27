#Primero pedimos los numeros
num1 = int(raw_input("Ingrese numero: "))
num2 = int(raw_input("Ingrese numero: "))
num3 = int(raw_input("Ingrese numero: "))
num4 = int(raw_input("Ingrese numero: "))

#Y luego los ordenamos
if (num1 <= num2 and num1 <= num3 and num1 <= num4) and (num4 >= num1 and num4 >= num2 and num4 >= num3): #num1 minimo, num4 maximo
	if num2 <= num3:
		print str(num1)+" "+str(num2)+" "+str(num3)+" "+str(num4)
	else:
		print str(num1)+" "+str(num3)+" "+str(num2)+" "+str(num4)

elif (num1 <= num2 and num1 <= num3 and num1 <= num4) and (num3 >= num1 and num3 >= num2 and num3 >= num4): #num1 minimo, num3 maximo
	if num2 <= num4:
		print str(num1)+" "+str(num2)+" "+str(num4)+" "+str(num3)
	else:
		print str(num1)+" "+str(num3)+" "+str(num4)+" "+str(num2)

elif (num1 <= num2 and num1 <= num3 and num1 <= num4) and (num2 >= num1 and num2 >= num3 and num2 >= num4): #num1 minimo, num2 maximo
	if num3 <= num4:
		print str(num1)+" "+str(num3)+" "+str(num4)+" "+str(num2)
	else:
		print str(num1)+" "+str(num4)+" "+str(num3)+" "+str(num2)


elif (num2 <= num1 and num2 <= num3 and num2 <= num4) and (num1 >= num2 and num1 >= num3 and num1 >= num4): #num2 minimo, num1 maximo
	if num3 <= num4:
		print str(num2)+" "+str(num3)+" "+str(num4)+" "+str(num1)
	else:
		print str(num2)+" "+str(num4)+" "+str(num3)+" "+str(num1)

elif (num2 <= num1 and num2 <= num3 and num2 <= num4) and (num3 >= num1 and num3 >= num2 and num3 >= num4): #num2 minimo, num3 maximo
	if num1 <= num4:
		print str(num2)+" "+str(num1)+" "+str(num4)+" "+str(num3)
	else:
		print str(num2)+" "+str(num4)+" "+str(num1)+" "+str(num3)

elif (num2 <= num1 and num2 <= num3 and num2 <= num4) and (num4 >= num1 and num4 >= num2 and num4 >= num3): #num2 minimo, num4 maximo
	if num1 <= num3:
		print str(num2)+" "+str(num1)+" "+str(num3)+" "+str(num4)
	else:
		print str(num2)+" "+str(num3)+" "+str(num1)+" "+str(num4)


elif (num3 <= num1 and num3 <= num2 and num3 <= num4) and (num1 >= num2 and num1 >= num3 and num1 >= num4): #num3 minimo, num1 maximo
	if num2 <= num4:
		print str(num3)+" "+str(num2)+" "+str(num4)+" "+str(num1)
	else:
		print str(num3)+" "+str(num4)+" "+str(num2)+" "+str(num1)

elif (num3 <= num1 and num3 <= num2 and num3 <= num4) and (num2 >= num1 and num2 >= num3 and num2 >= num4): #num3 minimo, num2 maximo
	if num1 <= num4:
		print str(num3)+" "+str(num1)+" "+str(num4)+" "+str(num2)
	else:
		print str(num3)+" "+str(num4)+" "+str(num1)+" "+str(num2)

elif (num3 <= num1 and num3 <= num2 and num3 <= num4) and (num4 >= num1 and num4 >= num2 and num4 >= num3): #num3 minimo, num4 maximo
	if num1 <= num2:
		print str(num3)+" "+str(num1)+" "+str(num2)+" "+str(num4)
	else:
		print str(num3)+" "+str(num2)+" "+str(num1)+" "+str(num4)


elif (num4 <= num1 and num4 <= num2 and num4 <= num3) and (num1 >= num2 and num1 >= num3 and num1 >= num4): #num4 minimo, num1 maximo
	if num2 <= num3:
		print str(num4)+" "+str(num2)+" "+str(num3)+" "+str(num1)
	else:
		print str(num4)+" "+str(num3)+" "+str(num2)+" "+str(num1)

elif (num4 <= num1 and num4 <= num2 and num4 <= num3) and (num2 >= num1 and num2 >= num3 and num2 >= num4): #num4 minimo, num2 maximo
	if num1 <= num3:
		print str(num4)+" "+str(num1)+" "+str(num3)+" "+str(num2)
	else:
		print str(num4)+" "+str(num3)+" "+str(num1)+" "+str(num2)

elif (num4 <= num1 and num4 <= num2 and num4 <= num3) and (num3 >= num1 and num3 >= num2 and num3 >= num4): #num4 minimo, num3 maximo
	if num1 <= num2:
		print str(num4)+" "+str(num1)+" "+str(num2)+" "+str(num3)
	else:
		print str(num4)+" "+str(num2)+" "+str(num1)+" "+str(num3)


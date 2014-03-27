#Pedimos los numeros
num1 = int(raw_input("Ingrese numero: "))
num2 = int(raw_input("Ingrese numero: "))
num3 = int(raw_input("Ingrese numero: "))

#Y los ordenamos
if num1 <= num2 and num1 <= num3:
	menor = num1
	if num2 <= num3:
		medio = num2
		mayor = num3
	else:
		medio = num3
		mayor = num2

if num2 <= num1 and num2 <= num3:
	menor = num2
	if num1 <= num3:
		medio = num1
		mayor = num3
	else:
		medio = num3
		mayor = num1

else:
	menor = num3
	if num1 <= num2:
		medio = num1
		mayor = num2
	else:
		medio = num2
		mayor = num1

print str(menor)+" "+str(medio)+" "+str(mayor)
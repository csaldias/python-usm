#Pedimos los numeros
num1 = int(raw_input("Ingrese num: "))
num2 = int(raw_input("Ingrese num: "))

#Sumamos todos los numeros entre los dos especificados
suma = 0
for i in range(num1+1, num2):
	suma += i

print "La suma es", suma
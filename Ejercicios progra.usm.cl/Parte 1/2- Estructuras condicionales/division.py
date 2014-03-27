#Primero, pedimos los numeros
dividendo = int(raw_input("Dividendo: "))
divisor = int(raw_input("Divisor: "))

#Y luego, evaluamos si la division es exacta o no, ademas de mostrar el cociente y resto.
if dividendo % divisor == 0:
	print "La division es exacta."
else:
	print "La division no es exacta."

print "Cociente: "+str(dividendo / divisor)
print "Resto: "+str(dividendo % divisor)
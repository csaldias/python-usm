from math import *

#Que departamento quiere consultar?
depto_str = raw_input("Que departamento desea consultar? ")

#Desarmamos el numero, necesitamos el piso y numero de depto.
numero = int(depto_str[-1])
if len(depto_str) == 4:
	piso = int(depto_str[:2])
else:
	piso = int(depto_str[:1])
precio = 0
#Ahora comenzamos con las condiciones.
if (depto_str == "807"):
	precio = 500 #Depto con precio fijo.
elif (piso == 1):
	precio = 100 #Todos los deptos del primer piso valen 100.
elif (piso == 25):
	precio = 400 #Todos los deptos del ultimo piso valen 400.
else:
	precio = 245 #Precio base para los deptos intermedios.
	if (numero == 0 or numero == 4):
		#Los deptos con vista al cerro tienen rebaja del 17%.
		precio *= 0.83
	elif (numero == 3 or numero == 7):
		#Lo deptos con vista al mar tienen aumento del 13%.
		precio *= 1.13

#Redondeamos el preio hacia abajo.
precio = floor(precio)

#Y mostramos.
print "El precio de este departamento es "+str(int(precio))	
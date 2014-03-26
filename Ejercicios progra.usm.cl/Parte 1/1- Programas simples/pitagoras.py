from math import *
#Primero, pedimos los catetos
a = int(raw_input("Ingrese cateto a: "))
b = int(raw_input("Ingrese cateto b: "))

#Calculamos el cateto faltante, y mostramos en pantalla
c = sqrt(a ** 2 + b ** 2)
print "la hipotenusa es "+str(c)
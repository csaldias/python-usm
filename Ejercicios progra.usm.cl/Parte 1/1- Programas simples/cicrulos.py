from math import *

#Pedimos el radio del circulo
radio = int(raw_input("Ingrese el radio: "))

#Luego calculamos el perimetro y area del circulo
perimetro = 2*pi*radio
area = pi*radio**2

#Y finalmente los mostramos en pantalla
print "Perimetro: "+str(perimetro)
print "Area: "+str(area)
#Primero, pedimos el anno
anno = int(raw_input("ingresa anno: "))

#Y comprobamos si acaso es bisiesto o no.
#Condiciones:
#1- Si es divisible por 4, es bisiesto.
#2- Si es divisible por 100 no es bisiesto, a menos de que tambien sea divisible por 400.
if anno % 4 == 0 and anno % 100 != 0 or anno % 400 == 0:
	print str(anno)+" es bisiesto"
else:
	print str(anno)+" no es bisiesto "
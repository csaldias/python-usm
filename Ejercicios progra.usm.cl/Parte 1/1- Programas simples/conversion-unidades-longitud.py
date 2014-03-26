#Primero pedimos la longitud en centimetros
long_cm = int(raw_input("Ingrese longitud: "))

#Y la convertimos a pulgadas utilizando 1 in = 2.54 cm
long_in = long_cm / 2.54
print str(long_cm)+" cm = "+str(long_in)+" in"
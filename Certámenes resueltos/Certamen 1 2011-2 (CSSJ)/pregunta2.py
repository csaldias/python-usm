#Primero, pedimos la distancia y el angulo de caida.
radio_caida = float(raw_input("Distancia: "))
angulo_caida = float(raw_input("Angulo: "))

#Luego, vemos donde caera.
#Cae en la pileta?
if radio_caida <= 7.0:
	print "PILETA"

#Cae en las areas verdes?
elif (20.0 <= radio_caida <= 35.0) and ((0.0 <= angulo_caida <= 45.0) or (90.0 <= angulo_caida <= 135.0) or (180.0 <= angulo_caida <= 225.0) or (270.0 <= angulo_caida <= 315.0)):
	print "AREA VERDE"

#Cae sobre el publico?
elif radio_caida <= 45.0 and (45.0 <= angulo_caida <= 90.0):
	print "PUBLICO"

#Cae sobre el cemento?
elif radio_caida <= 45.0:
	print "CEMENTO"

#Por descarte, cae fuera de la plaza
else:
    print "FUERA DE LA PLAZA"

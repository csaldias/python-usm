#Necesitamos el destino y la autonmia.
destino = raw_input("Destino: ")
autonomia = int(raw_input("Autonmia: "))

lugar = 0

if destino == "B":
	while lugar < 16: #B esta¡ en el lugar 16
		if lugar + autonomia == 5: #No debe acampar en el lugar 5
			lugar += autonomia - 1 #Asi que acampa en el lugar anterior
		else:
			lugar += autonomia

		if lugar < 16:
			print "Acampa en km "+str(lugar)
	print "Llega a B"

elif destino == "C":
	while lugar < 21:
		if lugar + autonomia == 5 or lugar + autonomia == 14: #Lugares no tan buenos para acampar
			lugar += autonomia - 1 #Asi que acampamos un lugar antes
		else:
			lugar += autonomia

		if lugar < 21:
			print "Acampa en km "+str(lugar)
	print "Llega a C"

#Cuantas universidades son?
num = int(raw_input("Numero de Universidades: "))

#Tenemos que llevar la cuenta de cuantas ues aceptan, rechazan o empatan.
total_acepta = 0
total_rechaza = 0
total_empate = 0

for i in range(num):
	#Algunas variables que usaremos
	aceptar = 0
	rechazar = 0
	nulo = 0
	blanco = 0

	#Y pedimos los votos hasta que salga una X.
	nombre = raw_input("Universidad: ")
	voto = raw_input("Voto: ")
	while voto != "X":
		if voto == "A":
			aceptar += 1
		elif voto == "R":
			rechazar += 1
		elif voto == "N":
			nulo += 1
		elif voto == "B":
			blanco += 1

		#Pedimos el siguiente voto. Si no lo hacemos, nos quedamos estancados en el while para siempre...
		voto = raw_input("Voto: ")

	#Resultado final?
	if (aceptar > rechazar): total_acepta += 1
	elif (aceptar < rechazar): total_rechaza += 1
	else: total_empate += 1

	print nombre+": "+str(aceptar)+" aceptan, "+str(rechazar)+" rechazan, "+str(blanco)+" blancos, "+str(nulo)+" nulos."
	print "" #Un espacio entre cada universidad.

print "Universidades que aceptan: "+str(total_acepta)
print "Universidades que rechazan: "+str(total_rechaza)
print "Universidades con empate: "+str(total_empate)
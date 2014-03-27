#Primero, debemos pedir los datos
juegos_a = int(raw_input("Juegos ganados por A: "))
juegos_b = int(raw_input("Juegos ganados por B: "))

#Luego, evaluamos el estado del juego
if (juegos_a >= 0 or juegos_b >= 0) and (juegos_a <= 7 and juegos_b <= 7):
	if juegos_a == 7 or juegos_b == 7:
		if abs(juegos_a - juegos_b) <= 2:
			if juegos_a == 7:
				print "Gana A"
			else:
				print "Gana B"
		else:
			print "Invalido"
	elif juegos_a == 6 or juegos_b == 6:
		if abs(juegos_a - juegos_b) >= 2:
			if juegos_a == 6:
				print "Gana A"
			else:
				print "Gana B"
		else:
			print "Aun no termina"
	else:
		print "Aun no termina"
else:
	print "Invalido"
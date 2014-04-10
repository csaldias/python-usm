#Parte b)

nombre_ganador = ""
puntaje_ganador = 0.0

nombre = raw_input("Nombre: ")
while nombre != "FIN":
	puntaje = float(raw_input("Puntaje: ")) #Solo pedimos los puntajes si el nombre no es FIN.
	if puntaje > puntaje_ganador:
		nombre_ganador = nombre
		puntaje_ganador = puntaje

	nombre = raw_input("Nombre: ")

print "El ganador es "+str(nombre_ganador)
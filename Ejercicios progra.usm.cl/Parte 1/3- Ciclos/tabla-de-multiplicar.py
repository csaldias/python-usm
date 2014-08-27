#Hacemos dos ciclos for, que vayan de 1 a 10
for y in range(1,11): #Eje y
	for x in range(1,11): #Eje x
		print str(x*y).rjust(4),
		#rjust() justifica el texto a la derecha
		#rellenando con espacios hasta llegar a
		#un largo de 4.
	print "" #Pasar a la linea de abajo
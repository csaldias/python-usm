#Vamos pidiendo las notas...
c1 = float(raw_input("C1: "))
c2 = float(raw_input("C2: "))

#Las primeras condiciones:
if (c1 > 9.0 and c2 > 9.0): #Si ambos certamenes son mayores a 9, aprueba automaticamente.
	print "Aprobado"
elif (c1 < 2.0 and c2 < 2.0): #Si ambos certamenes son menores a 2, reprueba automaticamente.
	print "Reprobado"
else:
	#Para este entonces, todavia tiene chances de pasar.
	c3 = float(raw_input("C3: "))
	promedio = (c1+c2+c3)/3.0
	
	#Veamos las condiciones:
	if (promedio < 3.0): #Reprueba
		print "Reprobado"
	elif (promedio >= 7.0): #Aprueba
		print "Aprobado"
	else:
		#Si no se cumple nada de lo anterior, rinde examen.
		examen = float(raw_input("Examen: "))
		if (examen >= 5.0): #Para aprobar, debe sacarse al menos un 5.0 en el examen.
			print "Aprobado"
		else: #El semestre se lo comio.
			print "Reprobado"
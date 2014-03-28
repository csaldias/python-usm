veces_ganadas = 0

#Son 8 intentos.
for i in range(1,9):
	num_par=0
	num_impar=0
	cuenta=0
	
	while cuenta<4: #Cuatro numeros por intento
		numero=int(raw_input(""))
		if numero > 10 and numero < 100:
			cuenta += 1
			if numero % 2 == 0 and (num_impar==2 or num_impar==0):
				num_par+=1 #Dos pares consecutivos
			elif numero %2!=0 and (num_par==2 or num_par==0):
				num_impar+=1 #Dos impares consecutivos
		else:
			print "Invalido"
	
	if num_par==2 and num_impar==2: #2 pares consecutivos y 2 impares consecutivos (o viceversa)
		print "Intento "+str(i)+": exitoso"
		veces_ganadas += 1
	else: #Pares + impares intercalados, por ejemplo.
		print "Intento "+str(i)+": no exitoso"

	if veces_ganadas == 3: #Ganas con 3 intentos exitosos
		break

if veces_ganadas == 3:
	print usted gano
else:
	print perdiste
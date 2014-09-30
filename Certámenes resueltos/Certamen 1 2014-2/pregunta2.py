#Primero, debo pedir el string de la hora
hora_binaria = raw_input("Ingrese hora en binario: ")

#Para pasar a formato decimal, debemos:
#-Separar, de alguna forma, cada bloque de digitos
#-Separar los bloques antes del 1111 y despues del 1111
#-Convertir el numero binario en decimal

#Llegamos al bloque 1111?
es_1111 = False
#Contador para los bloques de hora
cont_bloque = 0
#Variables para la hora y el minuto en formato decimal
hora_dec = 0
minuto_dec = 0
#En caso de que exista algun error en la hora, lo sabremos
error_hora = False

#Como los bloques tienen un largo fijo de 4 digitos, iteramos de 5 en 5
for i in range(0, len(hora_binaria), 5):
	#Cortamos el string original
	bloque = hora_binaria[i:i+4]

	#Verificamos si acaso este es nuestro bloque 1111:
	if bloque == "1111":
		es_1111 = True
		continue #Pasamos a la iteracion siguiente

	#Si ya pasamos del bloque 1111
	if es_1111: #lo mismo que if es_111 == True:
		numero_dec = 0
		exponente = 3
		#Convertimos el bloque binario a decimal
		for num in bloque:
			numero_dec += int(num)*(2**exponente)
			exponente-=1
		#Que bloque es este?
		if cont_bloque == 0: #Primer digito hora
			if numero_dec > 2: error_hora = True #Esta mal digitada?
			hora_dec += 10*numero_dec
		elif cont_bloque == 1: #Segundo digito hora
			if numero_dec > 4: error_hora = True #Esta mal digitada?
			hora_dec += numero_dec
		elif cont_bloque == 2: #Primer digito minuto
			if numero_dec > 6: error_hora = True #Esta mal digitada?
			minuto_dec += 10*numero_dec
		elif cont_bloque == 3: #Segundo digito minuto
			if numero_dec > 9: error_hora = True #Esta mal digitada?
			minuto_dec += numero_dec
		
		#Aumentamos la cuenta de bloques
		cont_bloque += 1

#Ahora, imprimo la hora en formato decimal
if error_hora:
	#Si la hora esta mal ingresada, aviso.
	print "La hora ingresada no es valida"
else:
	#La hora esta bien ingresada. La imprimo.
	if hora_dec >12: #PM
		if minuto_dec<10: #Si los minutos son menores a 10, agrego un 0 para mantener el formato
			print str(hora_dec-12)+":0"+str(minuto_dec)+" PM"
		else:
			print str(hora_dec-12)+":"+str(minuto_dec)+" PM"
	else: #AM
		if minuto_dec<10: #Si los minutos son menores a 10, agrego un 0 para mantener el formato
			print str(hora_dec-12)+":0"+str(minuto_dec)+" PM"
		else:
			print str(hora_dec-12)+":"+str(minuto_dec)+" PM"
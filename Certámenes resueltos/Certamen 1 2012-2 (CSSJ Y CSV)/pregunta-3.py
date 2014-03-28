#La manera mas simple de hacer el problema es mediante strings.
#Se puede hacer numericamente (sin manejo de strings), pero quizas es innecesariamente complejo.

contrasena = ""

while len(contrasena) < 4:
	numero = raw_input("numero: ")
	suma_digitos = 0
	
	if int(numero) < 0: #Si no es positivo, no nos sirve
		print "Incorrecto"
		continue #Pasa a la siguiente iteracion
	
	for digito in numero: #Sumamos los digitos
		suma_digitos+=int(digito)
	
	suma_digitos_unidad = int(str(suma_digitos)[-1]) #Obtenemos el digito de la unidad
	
	if suma_digitos_unidad%2!=0:
		contrasena+=str(suma_digitos_unidad) #Si no es par, lo agregamos

print "Contrasena "+contrasena
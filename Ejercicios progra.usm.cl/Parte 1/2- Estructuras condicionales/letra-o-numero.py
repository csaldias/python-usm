#Primero, obtenemos el caracter a evaluar
char = raw_input("Ingrese caracter: ")

#Para luego evaluar si es numero, letra o ninguno de los dos.
char_ascii = ord(char)
if char_ascii >= 48 and char_ascii <= 57:
	print "Es numero."
elif char_ascii >= 65 and char_ascii <= 90:
	print "Es letra mayuscula."
elif char_ascii >= 97 and char_ascii <= 122:
	print "Es letra minuscula."
else:
	print "No es letra ni numero."
#Primero, pedimos las palabras
palabra_1 = raw_input("Palabra 1: ")
palabra_2 = raw_input("Palabra 2: ")

#Luego, obtenemos su largo y comparamos para ver cual es la mas larga
largo_1 = len(palabra_1)
largo_2 = len(palabra_2)

if largo_1 > largo_2:
	print "La palabra "+palabra_1+" tiene "+str(largo_1 - largo_2)+" letras mas que "+palabra_2
elif largo_2 > largo_1:
	print "La palabra "+palabra_2+" tiene "+str(largo_2 - largo_1)+" letras mas que "+palabra_1
else:
	print "las dos palabras tienen el mismo largo"
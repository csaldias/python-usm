#Primero, pedimos los tres lados del triangulo
lado_a = float(raw_input("Ingrese a: "))
lado_b = float(raw_input("Ingrese b: "))
lado_c = float(raw_input("Ingrese c: "))

#Luego, comprobamos la desigualdad triangular y, si aplica, el tipo de triangulo
if (abs(lado_a - lado_c) < lado_b) and (lado_b < abs(lado_a + lado_c)):
	if (lado_a == lado_b) and (lado_b == lado_c):
		print "El triangulo es equilatero"
	elif (lado_a == lado_b) or (lado_a == lado_c) or (lado_b == lado_c):
		print "El ttriangulo es isoceles"
	elif (lado_a != lado_b) or (lado_a != lado_c) or (lado_b != lado_c):
		print "El triangulo es escaleno"
else:
	print "No es un triangulo valido"
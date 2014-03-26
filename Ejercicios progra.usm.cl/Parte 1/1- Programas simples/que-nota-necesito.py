#Primero, pedimos las notas.
c1 = int(raw_input("Ingrese nota certamen 1: "))
c2 = int(raw_input("Ingrese nota certamen 2: "))
nl = int(raw_input("Ingrese nota laboratorio: "))

#Luego, calculamos la nota de certamenes necesaria para tener nota final 60.
nc = (60 - nl * 0.3) / 0.7

#Y luego, la nota necesaria en el certamen 3.
c3 = 3 * nc - c1 - c2
print "Necesita nota "+str(c3)+" en el certamen 3"
#Pidamos el valor de x.
x = float(raw_input("x: "))

#Algunas variables que vamos a usar.
p = 0
n = 0
#Ahora pidamos los coeficientes hasta que salga FIN.
#Iremos calculando el polinomio a medida que nos van dando los coeficientes.
print "Coeficientes:"
msg = raw_input("")
while msg != "FIN":
	coef = float(msg)
	p += coef*(x**n)
	n+=1
	msg = raw_input("")

print "p(x) = "+str(p)
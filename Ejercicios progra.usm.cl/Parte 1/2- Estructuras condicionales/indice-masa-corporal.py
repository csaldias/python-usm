#Pedimos la estatura, peso y la edad de una persona
estatura = float(raw_input("Ingrese la estatura: "))
peso = float(raw_input("Ingrese el peso: "))
edad = float(raw_input("Ingrese la edad: "))

#Y calculamos el IMC de la persona
imc = peso/(estatura**2)
print "IMC: "+str(imc)
if edad < 45:
	if imc < 22.0:
		print "Su riesgo es bajo"
	else:
		print "Su riesgo es medio"
else:
	if imc < 22.0:
		print "Su riesgo es medio"
	else:
		print "Su riesgo es alto"
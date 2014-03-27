#Primero pedimos los 2 numeros y la operacion a realizar
num1 = int(raw_input("Operando: "))
operador = raw_input("Operador: ")
num2 = int(raw_input("Operando: "))

#Y luego realizamos la operacion pedida
if operador == "+":
	print str(num1)+" "+operador+" "+str(num2)+" = "+str(num1+num2)
elif operador == "-":
	print str(num1)+" "+operador+" "+str(num2)+" = "+str(num1-num2)
elif operador == "*":
	print str(num1)+" "+operador+" "+str(num2)+" = "+str(num1*num2)
elif operador == "**":
	print str(num1)+" "+operador+" "+str(num2)+" = "+str(num1**num2)
else:
	print str(num1)+" "+operador+" "+str(num2)+" = "+str(num1/(num2*1.0))
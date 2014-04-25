#Preguntamos la inversion inicial y la tasa de descuento
inversion_inicial = float(raw_input("Inversion inicial: "))
tasa = int(raw_input("% tasa de descuento: "))

#definimos algunas variables
van = -inversion_inicial #La inversion inicial es negativa
mes = 1
#Preguntamos por cada mes, hasta que VAN quede positivo.
while (van < 0):
	flujo_mes = int(raw_input("Flujo mes "+str(mes)+": "))
	van += flujo_mes/((1+(tasa/100.0))**mes)
	print "VAN: "+str(int(van)) #Mostramos la parte entera del float van
	mes+=1;
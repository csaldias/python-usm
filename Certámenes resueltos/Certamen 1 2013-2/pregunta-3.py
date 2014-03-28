ventas_larry = 0
ventas_curly = 0
ventas_moe = 0
opcion = 4

maxima_venta = 0
maximo_vendedor = ""

print "1.- Ingresar ventas"
print "2.- Venta mayor"
print "3.- Peor vendedor"
print "0.- Salir"

while opcion != 0:
	opcion = int(raw_input("Operacion? "))
	
	if opcion == 1:
		nombre = raw_input("Nombre vendedor: ")
		
		if nombre == "larry":
			venta = int(raw_input("Cantidad vendida: "))
			ventas_larry += venta
			if venta >= maxima_venta:
				maxima_venta = venta
				maximo_vendedor = "larry"
	
		elif nombre == "moe":
			venta = int(raw_input("Cantidad vendida: "))
			ventas_moe += venta
			if venta >= maxima_venta:
				maxima_venta = venta
				maximo_vendedor = "moe"
	
		else:
			venta = int(raw_input("Cantidad vendida: "))
			ventas_curly += venta
			if venta >= maxima_venta:
				maxima_venta = venta
				maximo_vendedor = "curly"
	
	elif opcion == 2:
		print "La mayor venta realizada fue de "+str(maxima_venta)+" y la realizo "+maximo_vendedor

	elif opcion == 3:
		minima_venta = min(ventas_curly,ventas_moe,ventas_larry)
		if minima_venta == ventas_larry:
			print "El vendedor que menos ha vendido es larry"
		elif minima_venta == ventas_curly:
			print "El vendedor que menos ha vendido es curly"
		else:
			print "El vendedor que menos ha vendido es moe"

print "moe vendio: "+str(ventas_moe)+" productos"
print "larry vendio: "+str(ventas_larry)+" productos"
print "curly vendio: "+str(ventas_curly)+" productos"
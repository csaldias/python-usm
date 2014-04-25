#Primero, pedimos los datos
n = int(raw_input("n: "))
cant_productos = int(raw_input("Cantidad productos: "))

#Las variables que vamos a usar
descuento = 20
total_compra = 0
total_descuento = 0
cont_productos = 0

for i in range(1, cant_productos+1):
	precio_producto = int(raw_input("Precio producto "+str(i)+": "))
	cont_productos += 1
	total_compra += precio_producto #Llevamos un contador del total de la compra sin descuentos
	total_descuento += int(precio_producto*(100 - descuento)/100.0) #Y llevamos otro contador de la compra con descuentos

	if n == cont_productos:
		cont_productos = 0
		if descuento != 5:
			descuento /= 2 #Cada n productos, el descuento se reduce a la mitad.
		else:
			descuento = 0 #Despues de un 5% de descuento, el descuento es cero.

print "Total: "+str(total_compra)
print "Descuento: "+str(total_compra - total_descuento)
print "Por pagar: "+str(total_descuento)

#NOTA: Los resultados que me da el programa son distintos a los que salen en el certamen, aun cuando los haga a mano. Es posible que el certamen tenga algun error.
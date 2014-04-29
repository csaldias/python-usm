#Primero, debemos pedir el año en curso.
anio_actual = int(raw_input("Ingrese anio en curso: "))

#Ahora vamos pidiendo los codigos hasta que el usuario ingrese "fin"
cod = raw_input("Ingrese un codigo: ")
while cod != "fin":
    #Desarmamos el codigo
    anio_ingreso = int(cod[:4])
    carrera = int(cod[4:7])
    ranking = int(cod[7:10])
    origen = int(cod[-2:])

    #Ahora vamos con las condiciones.
    #LLevaremos 2 variables, una para cada posibilidad de descuento. Al final, mantendremos la mas grande.
    descuento_1 = 0
    descuento_2 = 0

    #Primera condicion...
    if (anio_actual - anio_ingreso == 2): #Si lleva 2 años en la Universidad...
        descuento_1 += 5 #Es un descuento del 5%.
    elif (anio_actual - anio_ingreso == 3): #Si lleva 3 años en la Universidad...
        descuento_1 += 15 #Es un descuento del 15%.
    elif (anio_actual - anio_ingreso >= 4): #Si lleva 4 o mas años en la Universidad...
        descuento_1 += 25 #Es un descuento del 25%.

    #Segunda condicion...
    if (ranking <= 10): #Si ingreso dentro de los 10 primeros de su promocion...
        descuento_2 += 50 #Obtiene un 50% de descuento.
    elif (11 <= ranking <= 20): #Si esta entre los lugares 11 a 20...
        descuento_2 += 30 #es un 30%.
    elif (21 <= ranking <= 30): #Y si ingreso entre los lugares 21 a 30...
        descuento_2 += 10 #Es un 10%.

    descuento = max(descuento_1, descuento_2) #Solo nos interesa el mayor descuento de los dos.
    print "Al estudiante se le debe descontar un",descuento,"%"

    #Pedimos el siguiente codigo.
    cod = raw_input("Ingrese un codigo: ")
    

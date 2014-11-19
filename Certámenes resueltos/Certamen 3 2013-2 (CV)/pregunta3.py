def obtener_informacion(archivo,producto):
	#Abrimos el archivo de datos
	tienda = open(archivo)
	#Tomamos la primera linea, que tiene la ubicacion del establecimiento
	#Leemos, filtramos, separamos...
	ubicacion_string = tienda.readline().strip().split("#")
	#Pasamos a entero, y a tupla.
	ubicacion = tuple(map(float, ubicacion_string))
	#Definimos la variable de valor del producto. Por defecto, es cero.
	#asumiremos que no existen productos con valor cero. Si este valor es cero luego de leer el archivo, es porque no se encontro el producto.
	valor_producto = 0

	#Leemos el resto de las lineas, que tienen datos de productos
	for datos_producto in tienda:
		#Sacamos los datos del producto
		nombre_prod, categoria_prod, stock_prod, precio_prod = datos_producto.strip().split("#")
		#Si el nombre del producto es el buscado...
		if nombre_prod == producto:
			#Actualizamos la variable corespondiente
			valor_producto = int(precio_prod)

	tienda.close()
	#Veamos lo que tenemos que devolver...
	if valor_producto != 0: #El producto existen
		return (ubicacion, valor_producto)
	else: #El producto no existe
		return False

#Prueba
print obtener_informacion('falaferia.txt','Ipad')

#Debemos definir una funcion auxiliar para el punto b)
def calculo_distancia(punto1, punto2):
	#sqrt((x2-x1)^2 + (y2-y1)^2 )
	return ( (punto2[0]-punto1[0])**2 + (punto2[1]-punto1[1])**2 )**0.5

def calcular_distancia(lista, rut, ubicacion, producto):
    #Creamos el archivo con los datos del cliente
    archivo_cliente = open(rut+'.txt', 'w')
    #Creamos la variable que nos dira si se encontro el producto o no en alguna tienda
    #Asumiremos que el producto no existe a menos de que se demuestre lo contrario.
    producto_encontado = False
 
    #Comenzamos a buscar local por local
    for local in lista:
        #Obtenemos la info del producto en la tienda en cuestion
        datos_producto = obtener_informacion(local+'.txt', producto)
        #El producto existe en la tienda?
        if datos_producto != False:
            #Actualizamos la variable de control
            encontro_local = True
            #Desempaquetamos los datos
            ubicacion_local, precio_producto = datos_producto
            #Escribimos la linea correspondiente en el archivo
            archivo_cliente.write( producto + "@" + str(precio_producto) + "@" + local + "@" + str(calculo_distancia(ubicacion_local, ubicacion)) + "\n" )

    archivo_cliente.close()
	#Devolvemos si acaso encontramos o no el producto. 
    return encontro_local

#Prueba
print calcular_distancia(['Falaferia'],'11111111-1',(87.5, 45.7), 'Ipad')

def recomendar_establecimiento(lista, rut, ubicacion, producto):
    #Lo primero que hacemos es extraer los datos del producto
    datos_producto = calcular_distancia(lista, rut, ubicacion, producto)
    #Antes de hacer cualquier cosa: El producto existe en las tiendas especificadas?
    if datos_producto == False:
    	#No! No tiene caso seguir entonces.
        return False

    #El producto existe, por lo que existe un archivo rut.txt con todos los datos necesarios
    datos_cliente = open(rut + '.txt')
    #Definimos variables de menor distancia y menor precio
    menor_distancia = 99999.999999
    menor_precio = 9999999

    #Comenzamos la lectura
    for info_producto in datos_cliente:
    	#Filtramos la linea y desempaquetamos
        nombre_prod, precio_prod, local, distancia = info_producto.strip().split('@')
        #transformamos distancia y precio a float
        distancia = float(distancia)
        precio_prod = float(precio_prod)

        #Hacemos todas las comparaciones necesarias:
        #La distancia es mas chica que las menor de todas?
        if distancia < menor_distancia:
        	#Actualizamos
            menor_distancia = distancia
            #Guardamos la tienda mas cercana y el precio del producto
            tienda_mas_cercana = local
            precio_mas_cercano = precio_prod
		
		#El precio actual es mas chico que el menor de todos?  
        if precio_prod < menor_precio:
        	#Actualizamos
            menor_precio = precio_prod
            #Guadamos la tienda mas barata y su precio
            tienda_mas_barata = local
            distancia_mas_barata = distancia
 
    datos_cliente.close()

    #Ahora que tenemos todos los datos, podemos crear el archivo de recomendaciones.
    recomendaciones = open("recomendaciones.txt", "w")
 	#Escribimos todos los datos
    recomendaciones.write("Producto: " + producto + "\n")
    recomendaciones.write("Establecimiento con menor precio: " + tienda_mas_barata + "\n")
    recomendaciones.write("Precio: $" + str(menor_precio) + '\n')
    recomendaciones.write("Se encuentra a: " + str(distancia_mas_barata) +  "Km de distancia.\n")
    recomendaciones.write("Establecimiento mas cercano que tiene el producto: " + tienda_mas_cercana + "\n")
    recomendaciones.write("Precio: $" + str(precio_mas_cercano) + '\n')
    recomendaciones.write("Se encuentra a: " + str(menor_distancia) + " km de distancia\n")
 
    recomendaciones.close()
 	#Listo! Devolvemos True porque todo salio bien
    return True

#Prueba
print recomendar_establecimiento(['Falaferia'],'11111111-1',(87.5, 45.7), 'Ipad')
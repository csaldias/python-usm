def interpretar_geojson(linea):
	datos_interpretados = dict()
	#Primero, quitamos los dos "{" en ambos extremos de la linea, y separamos por ","
	datos = linea.strip("{").strip("}").split(",")
	#Iteramos sobre nuestro arreglo de datos:
	for dato in datos:
		#Separamos por ":"
		nombre, valor = dato.split(":", 1)
		#El 1 fuerza a split() a hacer solo 1 division en el string. Esto va a ser util cuando que tengamos que ver el dato de hora, que tiene ":" entre medio ademas del delimitador.
		#Debemos pasar cada valor a su tipo correspondiente:
		if nombre in ["mag", "dept"]: #A float
			datos_interpretados[nombre]= float(valor)
		elif nombre in ["tsunami"]: #A entero
			datos_interpretados[nombre]= int(valor)
		elif nombre in ["date"]: #A tupla de enteros
			fecha = valor.split("-") #['2014','03','17']
			anno, mes, dia = map(int, fecha) #[2014,03,17]
			datos_interpretados[nombre] = (anno, mes, dia)
		else: #A string
			datos_interpretados[nombre]= valor

	#Y devolvemos los datos interpretados
	return datos_interpretados

#Prueba
print  interpretar_geojson('{mag:5.8,place:Salvador,dept:23.0,tsunami:0,date:2014-03-17,time:06:11:08}')

def mayor_sismo(nombre_archivo):
	#Datos que debemos guardar
	mayor_magnitud = -99.9
	mayor_fecha = (1990, 12,30)
	mayor_lugar = "lolville"

	#Abrimos el archivo y leemos cada linea
	datos = open(nombre_archivo)
	for linea in datos:
		#Obtenemos el diccionario con los datos de la linea
		datos_sismo = interpretar_geojson(linea.strip())
		#La magnitud del sismo es mas grande que la mas grande registrada?
		if datos_sismo["mag"] >= mayor_magnitud:
			#Actualizamos todos los datos
			mayor_magnitud = datos_sismo["mag"]
			mayor_fecha = datos_sismo["date"]
			mayor_lugar = datos_sismo["place"]
	
	datos.close()
	#Ordenamos los datos y los dejamos presentables
	return (mayor_magnitud, mayor_lugar, mayor_fecha)

#Prueba
print mayor_sismo("registro.geojson")

def mostrar_registro(nombre_archivo, mag):
	#Abrimos el archivo y leemos cada linea
	datos = open(nombre_archivo)
	for linea in datos:
		#Obtenemos el diccionario con los datos de la linea
		datos_sismo = interpretar_geojson(linea.strip())
		#Si la magnitud del sismo es igual o mayor a la buscada, mostramos los datos.
		if datos_sismo["mag"] >= mag:
			lugar = datos_sismo["place"].upper() #Lugar, a mayusculas
			magnitud = str(datos_sismo["mag"]) #Magnitud, a string
			profundidad = str(datos_sismo["dept"]) #Profundidad, a string
			fecha_hora = "-".join(map(str,datos_sismo["date"]))+"-"+datos_sismo["time"] #WTF!?
			#map(str,datos_sismo["date"]) transforma los elementos de la tupla fecha de ser enteros a ser strings. Queda ('2014','3','15')
			#"-".join(asdf) une todos los elementos con "-". Queda '2014-3-15'
			#El resto de esa linea es facil de entender, creo yo...

			print lugar, "<->", magnitud, "<->", profundidad, "<->", fecha_hora

	datos.close()
	#La funcion no retorna nada
	return None

#Prueba
mostrar_registro("registro.geojson",4.4)
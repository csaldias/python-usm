#Datos del problema.
vuelos = {
140: ('Cancun', (2013, 6, 28), 6751),
141: ('Rio de Janeiro', (2013, 6, 13), 2772),
142: ('New York', (2013, 9, 12), 7546),
143: ('Tokio', (2013, 8, 17), 14248),
144: ('New York', (2014, 1, 1), 3792),
145: ('Rio de Janeiro', (2013, 12, 20), 2819),
146: ('Punta Cana', (2013, 8, 18), 5444)
}

itinerario = {
"Daniel": {140,146},
"Juan": {144,140},
"Rodrigo": {142,144,141},
"Pedro": {145,146}
}
 
#Pregunta a)
def vuelo_mas_tardio(vuelos):
    fecha_tardia = (0, 0, 0)
    #Iteramos sobre los valores del diccionario vuelos.
    for codigo_vuelo, datos_vuelo in vuelos.items():
        #Obtenemos la fecha
        _, fecha, _ = datos_vuelo
        #Si la fecha del vuelo es mayor a la fecha mas tardia...
        if fecha_tardia < fecha:
            #Actualizamos...
            fecha_tardia = fecha
            #Y guardamos el codigo del vuelo
            codigo_vuelo_tardio = codigo_vuelo
    return codigo_vuelo_tardio
 
 
# Pregunta b)
def kilometros_por_volar(pasajero, itinerario, vuelos):
    distancias = []
    #Obtenemos el itinerario del pasajero
    for codigo_vuelo in itinerario[pasajero]:
        #Obtenemos la distancia del vuelo, y la agregamos a nuestra lista
        distancias.append(vuelos[codigo_vuelo][2])
    return distancias
 
 
# Pregunta c)
def premio(itinerario, vuelos):
    premios = {}
    #Obtenemos el codigo del vuelo mas tardio
    codigo_vuelo_tardio = vuelo_mas_tardio(vuelos)
    #Iteramos sobre los nombres...
    for nombre in itinerario:
        #Para obtener su itinerario
        ruta = itinerario[nombre]
        #Si la persona compro el vuelo mas tardio...
        if codigo_vuelo_tardio in ruta:
            #Lo premiamos con un monto equivalente a la cantidad de km que
            #va a volar.
            distancias = kilometros_por_volar(nombre,itinerario,vuelos)
            premios[nombre]=sum(distancias)
    return premios

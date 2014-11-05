#Datos de prueba

#Aca, el esquema es: codigo_vuelo: (nombre_aerolinea, ciudad_partida, ciudad_destino, escalas, tiempo_promedio),
SansaVuelos = {
                'NH217': ('All Nipon Airways', 'Tokyo', 'Santiago', ['Atlanta'],
                        1620),
                'AY154': ('Finnair', 'Helsinki', 'Moscu', ['Riga'], 175),
                'OV171': ('Estonian Air', 'Tallin', 'Paris', ['Amsterdam',
                        'Berlin'], 205),
                # ...
                }

#Aca, el esquema es: id: (codigo_vuelo, fecha_vuelo)
Vuelo = {
        3542: ('AY154', (2013, 12, 25)),
        6433: ('NH217', (2013, 12, 31)),
        1313: ('NH217', (2013, 11, 6)),
        # ...
        }


def vuelo_entre_fechas(fecha1, fecha2, Vuelo):
    #Nos piden conjunto, hacemos un conjunto
    vuelos = set()

    #Iteramos sobre los vuelos. De aca, nos interesa el ID y la fecha
    for codigo_vuelo, fecha_vuelo in Vuelo.values():
        #La fecha esta entre las dos fechas pedidas?
        if fecha1 <= fecha_vuelo <= fecha2:
            #Si! Este vuelo nos sirve. Agregamos el codigo.
            vuelos.add(codigo_vuelo)

    #Listo! Devolvemos el conjunto de vuelos
    return vuelos

print vuelo_entre_fechas( (2013,7,22), (2014,7,22), Vuelo )

def vuelos_agotadores(fecha1, fecha2, Vuelo, SansaVuelos):
    #Nos piden conjunto, hacemos un conjunto.
    vuelos = set()
    
    #Obtenemos todos los vuelos que se hicieron en estas fechas, usando la funcion anterior.
    vuelos_realizados = vuelo_entre_fechas(fecha1, fecha2, Vuelo)

    #Iteramos sobre los vuelos que se hicieron entre ambas fechas.
    for vuelo in vuelos_realizados:
        #Obtenemos la info acerca del vuelo
        nombre_aerolinea, ciudad_partida, ciudad_destino, escalas, tiempo_promedio = SansaVuelos[vuelo]

        #Las condiciones del problema (ojo, tiempo_promedio esta en minutos!)
        if len(escalas) >= 3 or tiempo_promedio / 60.0 >= 8:
            #Este vuelo es agotador! Lo agregamos al conjunto
            vuelos.add(vuelo)

    #Listo! devolvemos el conjunto
    return vuelos

print vuelos_agotadores( (2013,7,22), (2014,7,22), Vuelo, SansaVuelos )

def vuelos(partida, destino, Vuelo, SansaVuelos):
    #Nos piden lista, hacemos una lista
    vuelos = []

    #Iteramos sobre los vuelos
    for codigo, (nombre_aerolinea, ciudad_partida, ciudad_destino, escalas, tiempo_promedio) in SansaVuelos.items():
 
        # Si las ciudades de partida y destino coinciden con las pedidas...
        if partida == ciudad_partida and destino == ciudad_destino:
            #Bien! Ahora buscamos en que fecha se realizo el vuelo
            fechas_vuelo = []
 
            #Recorremos Vuelo para obtener las fechas
            for codigo_vuelo, fecha_vuelo in Vuelo.values():
                #Si el codigo coincide con el del vuelo en cuestion...
                if codigo == codigo_vuelo:
                    #Lo encontramos! Agreguemoslo a la lista
                    fechas_vuelo.append(fecha_vuelo)
 
            # Ok! Ahora que tengo, todo, lo agergo como tupla a la lista final
            vuelos.append( (codigo, nombre_aerolinea, fechas_vuelo) )

    #Terminamos! Devolvamos la lista, y tamos listos. Por fin.
    return vuelos

print vuelos( 'Helsinki', 'Moscu', Vuelo, SansaVuelos )
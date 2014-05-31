#Los datos del problema.

salidas = [ ((2013,11,2), 'LAN123','NewYork','EMBARQUE'),
            ((2013,4,28), 'MX201', 'Cancun', 'ARRIBADO'),
            #...
            ]
 
vuelos = { 'LAN123': {'16740623-7', '1111111-1', '555555-5'},
            'ALGO00': {'444444-4'},
            'MX201': {'777777-7'},
            # ...
        }
 
personas = {'16740623-7':('OEncina', 'NewYork', (1987, 7, 22), 62000),
            '444444-4':('Edwar Lopez', 'Miami', (1900, 3, 11), 120000),
            '777777-7':('Jorge Perez', 'Santiago', (1989, 2, 17), 1000),
            '555555-5':('Daniela Perez', 'Roma', (1991, 8, 17), 12000),
            '1111111-1':('Sandra Lazo', 'Ibiza', (1970, 4, 14), 10000),
            # ...
            }
 
 
# Pregunta a)
def estado_pasajero(nombre):
    #Iteramos sobre el diccionario personas, y desempaquetamos todo
    for rut, datos in personas.items():
        nombre, ciudad_origen, fecha_nacimiento, millas = datos
        #Si esta es la persona que buscamos...
        if nombre_pasajero == nombre:
            #Revisamos los vuelos...
            for codigo_vuelo, rut_pasajeros in vuelos.items():
                #Si la persona esta en este vuelo...
                if rut in rut_pasajeros:
                    #Revisamos las salidas...
                    for datos_salida in salidas:
                        fecha_salida, codigo, ciudad, estado_vuelo = datos_salida
                        #Si encontramos el vuelo...
                        if codigo_vuelo == codigo:
                            #Devolvemos todos los datos.
                            return (rut, ciudad_de_origen, estado_vuelo)
    #Si no hay coincidencias, devolvemos None
    return None
 
 
# Pregunta b)
def cambia_de_vuelo(rut, nuevo_vuelo, millas):
    for codigo, ruts in vuelos.items():
        #Si el pasajero existe...
        if rut in ruts:
            #Quitamos al pasajero de su actual vuelo...
            ruts.remove(rut)
            #Y lo agregamos al nuevo vuelo. Recuerda que el diccionario vuelos
            #tiene como llave un string y como valor un conjunto, por lo que
            #usamos .add()
            vuelos[nuevo_vuelo].add(rut)
 
            #Sumamos las millas y actualizamos
            datos_persona = personas[rut]
            nombre, ciudad_origen, fecha_nacimiento, cantidad_millas = datos_persona
            cantidad_millas += millas
            datos_persona_actualizados = (nombre, ciudad_origen, fecha, cantidad_millas)
            personas[rut] = datos_persona_actualizados
 
            return True
    #Si el pasajero no existe, devolvemos False.
    return False
 
 
# Pregunta c)
def filtro_nac(fecha, estado):
    filtro = set()
    for rut, datos_persona in personas.items():
        #Solo necesitamos el nombre y la fecha de nacimiento, el resto de los
        #datos los podemos omitir.
        nombre, _, fecha_nacimiento, _ = datos_persona
        #Si la fecha de nacimiento es mayor a la pedida...
        if fecha < fecha_nacimiento:
            #Obtenemos los datos que necesitamos ocupando la primera funcion
            #(BTW, a los profes le gusta que hagas esto)
            _, _, estado_vuelo = estado_pasajero(nombre)
            #Si el estado es el pedido...
            if estado_vuelo == estado:
                #Lo agregamos
                filtro.add(rut)
    return conjunto
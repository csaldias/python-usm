#Datos de prueba
grupo = {
'rick': (172, 10), 'daryl': (136, 11), 'michonne': (80, 6),
'glenn': (73, 0), 'maggie': (55, 4), 'carl': (62, 1),
'tyreese': (35, 0), 'carol': (17, 3)}

def total(grupo):
    #Nuestras variables auxiliares. Notar el decimal!
    total_walkers = 0.0
    total_humanos = 0.0
    #Iteramos sobre los valores del grupo
    for walkers, humanos in grupo.values():
        #Vamos sumando...
        total_walkers += walkers
        total_humanos += humanos

    #Devolvemos todo en formato tupla
    return (total_walkers, total_humanos)

print total(grupo)

def puntaje(grupo):
    #Nuestro diccionario de puntajes
    puntajes = {}
    #Obtenemos el total de walkers y de humanos usando la funcion anterior
    total_walkers, total_humanos = total(grupo)

    for nombre, (walkers, humanos) in grupo.items():
        #Calculamos el puntaje con la formula del enunciado
        puntaje = (walkers / total_walkers) + 2 * (humanos / total_humanos)
        #Los valores van a quedar con mas decimales que los del certamen!
        #Una opcion es redondear los ptjes a 2 deimales
        puntajes[nombre] = round(puntaje,2)

    #Devolvemos el diccionario con los puntajes
    return puntajes
print puntaje(grupo)

def ranking(grupo):
    #Nuestras variables auxiliares
    puntajes_ordenados = []
    nombres_ordenados = []

    #Obtenemos los puntajes por persona usando la funcion anterior
    puntajes = puntaje(grupo)

    #Iteramos el diccionario de puntajes para convertirlo en una lista de tuplas.
    #Para que? Sigue leyendo...
    for nombre, puntaje_persona in puntajes.items():
        puntajes_ordenados.append( (puntaje_persona, nombre) )

    #Convertimos el diccionario a una lista de tuplas para poder ordenarla usando sort()
    #Como el puntaje quedo primero en la tupla, sort() ordenara la lista en base al puntaje.
    #Como sort() ordena de menor a mayor, la damos vuelta con reverse()
    puntajes_ordenados.sort()
    puntajes_ordenados.reverse()

    #Ok, ahora tenemos una lista de tuplas ordenada con los puntajes de mayor a menor, junto al nombre
    #asociado a cada puntaje. Nos queda pasar todos esos nombres, en el mismo orden, a otra lista, y listo!
    for puntaje_persona, nombre in puntajes_ordenados:
        nombres_ordenados.append(nombre)

    #Terminamos! Ahora, devolvemos la lista de nombres.
    return nombres_ordenados

print ranking(grupo)
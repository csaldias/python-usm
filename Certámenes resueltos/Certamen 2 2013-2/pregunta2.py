#Datos de ejemplo del problema.
series = [
('game of thrones', 'USA', 9.4, ['ficcion']),
('24', 'USA', 8.4, ['accion','suspenso']),
('orange is the new black', 'USA', 8.5, ['comedia','drama']),
('sherlock', 'UK', 9.2, ['policial','drama','suspenso']),
('whitecollar', 'USA', 8.2, ['comedia','drama','suspenso']),
('heroes', 'USA', 7.7, ['ficcion','accion']),
('mistfit', 'UK', 8.4, ['accion','drama','ficcion'])
# ...
]
 
#Problema a)
def series_por_pais(pais, series):
    series_pais = []
    #Iteramos sobre la lista de series
    for serie in series:
        #Desempaquetamos los datos
        nombre_serie, pais_de_origen, rating, generos = serie
        #Si el pais de origen es el buscado...
        if pais_de_origen == pais:
            #Lo agregamos a la lista
            series_pais.append( (nombre_serie, rating) )
    return series_pais

#Problema b)
def series_por_generos(generos, series):
    series_genero = set()
    #Iteramos sobre la lista de series
    for serie in series:
        #Desempaquetamos los datos
        nombre_serie, pais_de_origen, rating_serie, generos_serie = serie
        #Iteramos sobre una lista de generos pedidos
        for genero in generos:
            #Si la serie analizada es del (o los) genero(s) pedido(s)...
            if genero in generos_serie:
                #Lo agregamos al conjunto
                series_genero.add( (nombre, rating) )
    return series_genero

#Problema c)
def recomendaciones(pais, generos, series):
    #Algo que le gusta mucho a los profes: usar las funciones que creaste anteriormente.
    #Eso no significa que tengas que tenerlas hechas, solo saber que es lo que devuelven.
    lista_series_por_pais = series_por_pais(pais, series)
    conjunto_series_por_generos = series_por_generos(generos, series)
    #Aca conviene pasar la lista de series por pais a conjunto, porque asi podemos
    #sacar la interseccion para obtener las series que cumplan tanto con el requisito
    #de pais como de genero.
    conjunto_series_por_pais = set(lista_series_por_pais)
    series_en_comun = conjunto_series_por_generos & conjunto_series_por_pais
    #Ahora queda buscar el que tenga mas rating, y tamos listos.
    mayor_rating = -999
    for serie in series_en_comun:
        nombre_serie, rating = serie
        #Hacemos la comparacion
        #Si el rating de la serie es mas grande que el rating mas grande conocido...
        if rating > mayor:
            #Actualizo mi contador...
            mayor_rating = rating
            #Y actualizo el nombre de la serie a recomendar.
            serie_recomendada = nombre_serie
    return serie_recomendada
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
 
 
# Funcion a)
def series_por_pais(pais, series):
    lista = []
 
    for serie in series:
        # Desempaquetado
        nombre, pais_de_origen, rating, generos = serie
 
        if pais_de_origen == pais:
            tupla = (nombre, rating)
            lista.append(tupla)
 
    return lista
 
 
# Funcion b)
def series_por_generos(generos, series):
    conjunto = set()
 
    for serie in series:
        nombre, pais_de_origen, rating, generos_serie = serie
 
        # Se recorre la lista de generos entregados por el parametro para ver si
        # al menos uno esta dentro de la lista de generos de la serie
        for genero in generos:
 
            if genero in generos_serie:
                tupla = (nombre, rating)
                conjunto.add(tupla)
 
    return conjunto
 
 
# Funcion c)
def recomendaciones(pais, generos, series):
    # En este caso conviene bastante usar las funciones anteriores en vez de
    # realizar nuevamente si una serie tiene un genero determinado o si proviene
    # de tal pais. Es por esto que vamos a guardar la lista y el conjunto de las
    # funciones a) y b) respectivamente en dos variables distintas.
 
    lista_series_por_pais = series_por_pais(pais, series)
    conjunto_series_por_generos = series_por_generos(generos, series)
 
    # Ahora solo hay que buscar entre ambos tipos de datos aquel que este en
    # ambos y que sea el de mayor puntuacion
 
    # En este caso elegi convertir a conjunto la lista series_por_pais e
    # intersectarla con el otro conjunto para ver aquellos elementos en comun
    conjunto_series_por_pais = set(lista_series_por_pais)
 
    series_en_comun = conjunto_series_por_generos & conjunto_series_por_pais
 
    # Ahora vamos en busca del que tiene mayor rating
    mayor = -999999
    for serie in series_en_comun:
        nombre, rating = serie
 
        if rating > mayor:
            mayor = rating
            nombre_serie_recomendada = nombre
 
    return nombre_serie_recomendada
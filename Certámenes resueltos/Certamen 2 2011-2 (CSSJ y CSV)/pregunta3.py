#Diccionario con los usuarios de tuiton

tuiton = {
# usuario: conjunto de usuarios a quienes sigue
'@progra_usm': {'@kena123', '@anamontain'},
'@luismi': {'@huaiqui', '@jvivar'},
'@jvivar': {'@anamontain', '@progra_usm'},
'@huaiqui': {'@anamontain', '@luismi'},
'@anamontain': {'@luismi', '@progra_usm', '@huaiqui'},
'@kena123': {'@luismi', '@huaiqui'}
# ...
}

# Pregunta a)
def numero_de_seguidores(usuario, tuiton):
    #Definimos un contador
    contador = 0
    #Recorremos el diccionario de usuarios.
    #tuiton.items nos da una lista de tuplas, asi que las desempaquetamos.
    for nombre, seguidores in tuiton.items():
        #Si la persona es seguida por alguien...
        if usuario in seguidores:
            #Aumentamos el contador.
            contador += 1
    return contador


# Pregunta b)
def son_amigos(usuario1, usuario2, tuiton):
    #Asi vemos, de una forma rapida, si dos usuarios se siguen mutuamente:
    #Si usuario1 esta en el conjunto de personas seguidas por usuario2,
    #Y usuario 2 esta en el conjunto de personas seguidas por usuario1...
    if usuario1 in tuiton[usuario2] and usuario2 in tuiton[usuario1]:
        #Devuelvo verdadero.
        return True
    else:
        #En otro caso, devuelvo falso.
        return False

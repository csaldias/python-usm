#Primero, pedimos las anotaciones
anotaciones = raw_input("Anotaciones: ")

#Definimos los contadores que necesitamos
total_puntos = 0
total_periodo = 0
periodo_actual = 1

for i in range(len(anotaciones)):
    letra_actual = anotaciones[i]
    if letra_actual == "L":
        total_periodo += 1
    elif letra_actual == "D":
        total_periodo += 2
    elif letra_actual == "T":
        total_periodo += 3
    elif letra_actual == " ":
        #Terminamos este periodo y pasamos al siguiente
        print str(total_periodo)+" puntos en el periodo "+str(periodo_actual)
        total_puntos += total_periodo
        total_periodo = 0
        periodo_actual += 1

#Al final, imprimimos los puntos totales.
#Ojo que el ciclo de arriba no va a imprimir el puntaje del ultimo periodo, ya que el ultimo caracter de la palabra no es un espacio.
print str(total_periodo)+" puntos en el periodo "+str(periodo_actual)
total_puntos += total_periodo
print "Total: "+str(total_puntos)+" puntos"

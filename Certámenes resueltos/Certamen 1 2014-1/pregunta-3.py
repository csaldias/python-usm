#Pedimos la ruta
ruta = raw_input("Ruta: ")

#El truco esta en pensar que el robot se encuentra en el centro de un sistema de coordenadas cartesianas.
#En ese caso, el robot estaria en el (0,0).
#Cada letra, ya sea n, s, o y e, suman o restan una unidad en el eje x o y.
pos_x = 0
pos_y = 0

#Iteramos sobre la ruta dada.
for orden in ruta:
    if orden == 'n':
        pos_y += 1
    elif orden == 's':
        pos_y -= 1
    elif orden == 'o':
        pos_x -= 1
    elif orden == 'e':
        pos_x += 1

#Para este punto, tendremos las coordenadas del pto de destino.
#Como el robot partio del (0,0), la forma mas eficiente de dirigirse hasta el pto de destino
#es decirle al robot que vaya a esas coordenadas.
#Ejemplo: si el pto de destino es el (1,-2), significa que el robot debe bajar 2 espacio y moverse 1 espacio hacia la derecha, y asi habra llegado de la forma mas eficiente.

ruta_optima = ""
if pos_x >= 0:
    ruta_optima += "e"*pos_x
elif pos_x < 0:
    ruta_optima += "o"*abs(pos_x)
if pos_y >= 0:
    ruta_optima += "n"*pos_y
elif pos_y < 0:
    ruta_optima += "s"*abs(pos_y)

print "Ruta optima:",ruta_optima

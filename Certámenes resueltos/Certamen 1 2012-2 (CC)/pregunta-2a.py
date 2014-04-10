#Parte a)

nombre = raw_input("Nombre: ")
grado_dif = float(raw_input("Grado de dificultad: "))

puntaje_max = -20.0
puntaje_min = 20.0
puntaje_suma = 0.0

for i in range(1,8): #Pedimos siete puntajes de siete jueces
	puntaje = float(raw_input("Juez "+str(i)+": "))
	puntaje_suma += puntaje
	if puntaje > puntaje_max: puntaje_max = puntaje
	if puntaje < puntaje_min: puntaje_min = puntaje

puntaje_total = (puntaje_suma - puntaje_max - puntaje_min)*0.6*grado_dif
print "El puntaje total es "+str(puntaje_total)
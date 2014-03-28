#Pedimos los datos de la bateria
capacidad = int(raw_input("Capacidad bateria (AH): "))
voltaje = int(raw_input("Voltaje bateria (Volt): "))
base = int(raw_input("Base de tiempo (Horas): "))

autonomia = 99999
ampolletas = 0
potencia_total = 0
#Ahora pedimos las ampolletas hasta que la autonomia sea menor a 8 horas.

while autonomia >= 8:
	potencia = float(raw_input("Potencia ampolleta "+str(ampolletas+1)+" (Watt): "))
	#Calculamos la autonomia
	potencia_total += potencia
	consumo = potencia_total / voltaje
	autonomia = base / (((consumo * base) / capacidad) ** 1.15)
	if autonomia >= 8:
		ampolletas += 1
		print "Autonomia: "+str(autonomia)+" [Horas]. Ampolletas: "+str(ampolletas)+". Potencia total: "+str(potencia_total)+" [Watt]"

print "Total de ampolletas: "+str(ampolletas)
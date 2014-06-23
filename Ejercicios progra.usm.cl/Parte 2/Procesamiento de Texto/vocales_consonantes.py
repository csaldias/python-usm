def es_vocal(letra):
	if letra in 'aeiou':
		return True
	else:
		return False

def contar_vocales_y_consonantes(palabra):
	cuenta_vocal = 0
	cuenta_consonante = 0
	for letra in palabra:
		if es_vocal(letra):
			cuenta_vocal += 1
		else:
			cuenta_consonante += 1
	return (cuenta_vocal, cuenta_consonante)

palabra = raw_input("Ingrese palabra: ")
vocal, consonante = contar_vocales_y_consonantes(palabra)
print "Tiene", vocal, "vocales y", consonante, "consonantes"
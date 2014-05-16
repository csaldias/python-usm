pronombres = ['yo', 'tu', 'el', 'nosotros', 'vosotros', 'ellos']
 
conjugacion = {
	'ar': ('o', 'as', 'a', 'amos', 'ais', 'an'),
	'er': ('o', 'es', 'e', 'emos', 'is', 'en'),
	'ir': ('o', 'es', 'e', 'imos', 'is', 'en')
}

#Pedimos el verbo 
verbo = raw_input("Ingrese verbo: ")

#Separamos el verbo en prefijo y sufijo
prefijo = verbo[:-2]
sufijo = verbo[-2:]
 
for i in range(len(pronombres)):
	#Aqui es donde la magia ocurre (?!)	
    print pronombres[i] + " " + prefijo + conjugacion[sufijo][i]
#Solo para probar
paises = {
    'Pepito': {'Chile', 'Argentina'},
    'Yayita': {'Francia', 'Suiza', 'Chile'},
    'John': {'Chile', 'Italia', 'Francia', 'Peru'},
}

#Definimos la funcion
def cuantos_en_comun(a, b):
	#Cuantos elementos en comun entre 2 conjuntos?
    num = len((paises[a] & paises[b]))
    return num
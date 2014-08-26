def suma_lineas(datos1):
    lista=[]
    archivo=open("datos1.txt")
    for linea in archivo:
        lista.append(sum(map(int, linea.split())))
    archivo.close()
    return lista

print suma_lineas("datos1.txt")
raw_input("Presione una tecla para continuar...")
#Empezamos a pedir opciones.
resultado = raw_input("")

caras = 0
sellos = 0
intercalado = 0

#Inicializamos los contadores, dependiendo del resultado que haya salido. 
if resultado == 'C':
    caras = 1
elif resultado == 'S':
    sellos = 1

resultado_anterior = resultado

while caras < 4 and sellos < 4 and intercalado < 3:
    resultado = raw_input("")
 
    # Si hay dos C seguidas, se reinicia a 0 la variable intercalado y suma 1 al contador de caras.
    if lado == 'C' and  resultado_anterior == 'C':
        caras += 1
        sellos = 0
        intercalado = 0
 
    # Si hay dos S seguidas, se reinicia a 0 la variable intercalado y suma 1 al contador de sellos.
    elif lado == 'S' and resultado_anterior == 'S':
        sellos += 1
        caras = 0
        intercalado = 0
 
    # Si el resultado anterior es distinto al actual, se le suma 1 al contador intercalado y se reinicia a 0 el contador del lado que no salio ahora.
    elif (lado == 'C' and resultado_anterior == 'S'):
        intercalado += 1
        caras  = 1
        sellos = 0

    elif (lado == 'S' and resultado_anterior == 'C'):
        intercalado += 1
        caras  = 0
        sellos = 1
    # El resultado actual pasa a ser el resultado anterior
    resultado_anterior = resultado

#Y terminamos.
if intercalado == 3:
    print "Usted gano"
 
elif caras == 4 or sellos == 4:
    print "Usted perdio"
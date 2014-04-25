#Pedimos los datos que necesitamos.
alfil_fila = int(raw_input("Fila alfil: "))
alfil_columna = int(raw_input("Columna alfil: "))
torre_fila = int(raw_input("Fila torre: "))
torre_columna = int(raw_input("columna torre: "))
 
alfil_captura = 0
torre_captura = 0
 
#Ahora vemos quien captura a quien.
#El de la torre es simple: captura a alguien si esta en su misma fila o columna.
if alfil_fila == torre_fila or alfil_columna == torre_columna:
    torre_captura = 1

#Comprobar si acaso el alfil captura se ve complicado, pero en realidad es bien facil.
if abs(alfil_columna - torre_columna) == abs(alfil_fila - torre_fila):
    alfil_captura = 1

if alfil_captura == 1:
    print "Alfil captura"
if torre_captura == 1:
    print "Torre captura"
elif alfil_captura == 0 and torre_captura == 0:
    print "Ninguna captura"
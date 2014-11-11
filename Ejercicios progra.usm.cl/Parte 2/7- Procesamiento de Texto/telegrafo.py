#Pedimos el mensaje
msj = raw_input("Mensaje: ").lower()
costo = 0

#Quitamos los saltos de linea y los espacios del mensaje
msj_filtro = msj.replace(" ","").replace("\n","")

for letra in msj_filtro:
   	#if letra in 'qwertyuiopasdfghjklzxcvbnm'
    if ord(letra) in range(97,123):
        costo += 10
    #elif letra in '1234567890'
    elif ord(letra) in range(48,58):
        costo += 20
    else:
        costo += 30
print "Su mensaje cuesta $" + str(costo)
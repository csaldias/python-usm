#Pedimos el mensaje
msj = raw_input("Mensaje: ").lower()
costo = 0

for letra in msj:
    if letra != ' ':
    	#if letra in 'qwertyuiopasdfghjklzxcvbnm'
        if ord(letra) in range(97,123):
            costo += 10
        #elif letra in '1234567890'
        elif ord(letra) in range(65,91):
            costo += 20
        else:
            costo += 30
print "Su mensaje cuesta $" + str(costo)
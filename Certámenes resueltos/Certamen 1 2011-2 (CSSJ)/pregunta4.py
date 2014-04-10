#Pedimos el primer numero.
num = int(raw_input())

#Definimos nuestras variables.
num_numeros = 1
anterior = num 
ganar = False
 
while True:
    #Pedimos numeros constantemente hasta que algo pase...
    num = int(raw_input())
 
    if num == anterior:
        num_numeros += 1 #Si este numero es igual al anterior, +1 a la cuenta
    else:
        num_numeros = 1 #Si no, reiniciamos la cuenta
 
    if num == 1: #Si es un 1, fin de juego.
        break
 
    if num_numeros == num: #Si la cantidad de numeros es igual al numero, ganas.
        ganar = True
        break
 
    anterior = num
 
if ganar:
    print "Usted gano"
else:
    print "Usted perdio"

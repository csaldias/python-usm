#Pedimos la cantidad de numeros a ingresar
n = int(raw_input("Ingrese n: "))

#Definimos donde guardaremos el numero mayor
numero_mayor = 0

for i in range(n):
    #Pedimos cada numero
    numero = int(raw_input("Ingrese numero: "))
    #El numero actual es mayor que el mas grande conocido?
    if numero > numero_mayor:
        #Actualizamos la variable
        numero_mayor = numero

print "El mayor es", numero_mayor

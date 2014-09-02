#Pedimos un numero
numero = int(raw_input("Ingrese numero: "))

#Luego, generamos todos los numeros entre 1 y el numero ingresado
for i in range(1, numero+1):
    #Si el numero no es multiplo de 3 ni de 7...
    if i%3!=0 and i%7!=0:
        #Lo imprimimos
        print i

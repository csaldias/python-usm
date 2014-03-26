#Primero, pedimos el numero
num = float(raw_input("Ingrese un numero: "))

#Calculamos la parte entera, y se la restamos al numero.
num_entero = int(num)
num_decimal = abs(num) - abs(num_entero)
print num_decimal
#Productos especiales: Potencia factorial creciente

#Pedimos los numeros
n = int(raw_input("Ingrese n: "))
m = int(raw_input("Ingrese m: "))

#Calculamos la potencia
potencia = n
for i in range(1,m):
    potencia *= (n + i)

print potencia

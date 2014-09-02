#Productos especiales: Factorial

#Pedimos el numero
n = int(raw_input("Ingrese n: "))

#Calculamos el factorial de n
factorial = 1
for i in range(1,n+1):
    factorial = factorial * i

print factorial

from math import *
#Productos especiales: Numero de Stirling del Segundo tipo

#Pedimos los numeros
n = int(raw_input("Ingrese n: "))
k = int(raw_input("Ingrese k: "))

#Iremos calculando el Numero de Stirling por partes.
stirling = 0

#Primero, el factorial
factorial_k = 1
for i in range(1,k+1):
    factorial_k *= i

#Ahora, la sumatoria
suma = 0
for i in range(k+1):
    #Calculamos los tres factoriales del coeficiente binomial
    fact_k = 1
    for j in range(1,k+1):
        fact_k *= j
    
    fact_i = 1
    for j in range(1,i+1):
        fact_i *= j
    
    fact_k_i = 1
    for j in range(1, k-i+1):
        fact_k_i *= j
    
    #Ahora, calculamos el coeficiente binomial
    coef_binomial = fact_k / ( fact_k_i * fact_i )

    #Y el elemento de la suma
    suma += (-1)**i * coef_binomial * (k - i)**n

#Ahora nos queda dividir la suma por el factorial de k.
stirling = suma / factorial_k

print stirling
        

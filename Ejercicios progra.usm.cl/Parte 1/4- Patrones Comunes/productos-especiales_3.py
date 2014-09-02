#Productos especiales: Coeficiente Binomial

#Pedimos n y k
n = int(raw_input("Ingrese n: "))
k = int(raw_input("Ingrese k: "))

#Calculamos los tres factoriales del coeficiente binomial
fact_n = 1
for i in range(1,n+1):
    fact_n *= i

fact_k = 1
for i in range(1,k+1):
    fact_k *= i

fact_n_k = 1
for i in range(1, n-k+1):
    fact_n_k *= i

#Ahora, calculamos la fraccion
coef = fact_n / ( fact_n_k * fact_k )

print coef

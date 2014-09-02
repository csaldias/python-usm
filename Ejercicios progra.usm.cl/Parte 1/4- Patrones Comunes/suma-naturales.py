#Pedimos n
n = int(raw_input("Ingrese n: "))

#Calculamos las dos formulas pedidas
suma_1 = 0
suma_2 = 0

#S1
for i in range(1,n+1):
    suma_1 += i

#S2
suma_2 = ( n * (n + 1) ) / 2

#Mostramos ambos resultados
print "S1:", suma_1
print "S2:", suma_2

#Son iguales?
if suma_1 == suma_2:
    print "Son iguales"
else:
    print "No son iguales"

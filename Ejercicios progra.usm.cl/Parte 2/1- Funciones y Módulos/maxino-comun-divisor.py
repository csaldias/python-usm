#Funcion 1: MCD por metodo "tradicional"
def mcd_tradicional(a,b):
    maximo_divisor = 0
    #Probamos divisores desde el 1 hasta el menor de (a, b)
    for divisor in range(1, min(a,b)+1):
        if a%divisor == 0 and b%divisor == 0:
            maximo_divisor = divisor
    return maximo_divisor
 
#Funcion 2: MCD por Algoritmo de Euclides
#(Gracias, Wikipedia!)
def mcd_euclides(a,b):
    r0 = a
    r1 = b
    while True:
        resto = r0%r1
        if resto == 0:
            return r1
        else:
            r0 = r1
            r1 = resto

#Prueba 
print mcd_tradicional(20,50)
print mcd_euclides(31,19)
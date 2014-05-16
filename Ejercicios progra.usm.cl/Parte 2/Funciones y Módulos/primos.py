#Modulo con todas las funciones de funciones-numeros-primos.py
#para usarlas en mersenne.py
if __name__ == '__main__':
    print primeros_primos(20)

def es_divisible(n, d):
	#Parecida a la funcion del numero par.
	if n % d == 0:
		return True
	else:
		return False

def es_primo(n):
	#Un numero es primo si es divisible solo por el 1 y el mismo.
	#Por lo tanto, si encontramos otro divisor de nuestro numero
	#distinto a los dos de mas arriba, el numero no es primo.
	es_primo = True
	for i in range(2,n):
		if es_divisible(n,i):
			es_primo = False
	return es_primo

def i_esimo_primo(i):
	contador = 0
	n = 1
	while contador < i:
		n += 1
		if es_primo(n):
			contador += 1
	return n

def primeros_primos(m):
    primos = []
    for i in range(1, m + 1):
        primos.append(i_esimo_primo(i))
    return primos

def primos_hasta(m):
	lista_primos=[]
	for num in range(2,m+1):
		if es_primo(num):
			lista_primos.append(num)
	return lista_primos
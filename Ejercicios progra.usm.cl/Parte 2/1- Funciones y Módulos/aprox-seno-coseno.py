from math import *

def factorial_reciproco(n):
	return 1/factorial(n)

def signo(n):
	if n % 2 == 0:
		return 1
	else:
		return -1

def seno_aprox(x, m):
	suma = 0
	termino = 1
	for i in range(m):
		suma += signo(i)*(x**termino)*factorial_reciproco(termino)
		termino += 2
	return suma

def coseno_aprox(x, m):
	suma = 0
	termino = 0
	for i in range(m):
		suma += signo(i)*(x**termino)*factorial_reciproco(termino)
		termino += 2
	return suma

def error(f_exacta, f_aprox, m, x):
	return abs(f_exacta(x)-f_aprox(x, m))
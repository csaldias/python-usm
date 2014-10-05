from primos import *

total = int(raw_input('Cuantos primos de Mersenne: '))
p = 2
num = 0
while num < total:
    if es_primo(2**p-1) and es_primo(p):
        print 2**p - 1
        num += 1
    p += 1
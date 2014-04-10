#Primero, pedimos la palabra.
palabra = raw_input("Palabra: ")

#Luego, la recorremos para abreviarla.
#Definimos nuestras variables
abreviacion = "" #La palabra abreviada
palabra_actual = palabra[0] #La palabra que estaremos contando
contador = 0 #Cuantas palabras hemos contado

for i in range(len(palabra)):
    if palabra[i] == palabra_actual: #Si son iguales, contamos una mas
        contador += 1

    else: #Si es distinta, comenzamos a contar de nuevo
        abreviacion += str(contador)+palabra_actual
        contador = 1
        palabra_actual = palabra[i]

#Ojo, que la ultima parte de la abreviacion no se va a sumar en el ciclo de arriba, asi que debemos hacerlo afuera.
abreviacion += str(contador)+palabra_actual
print abreviacion

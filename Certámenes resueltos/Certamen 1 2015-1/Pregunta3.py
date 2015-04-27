#Punto a)
def ordenado(n):
    #Pasamos el numero a string, para que todo sea mas facil
    num_str = str(n)
    #Obtenemos el largo del numero
    num_len = len(num_str)

   	#Para comprobar si el numero esta ordenado de mayor a menor, debemos ir verificando que
   	#el numero siguiente sea siempre menor al numero anterior. Para eso, guardamos un digito
   	#del numero, y lo comparamos con el digito siguiente.

    #Guardamos el primer digito
    digito_1 = int(num_str[0])
    #Llevamos un contador de la posicion del digito a comparar
    digito = 1
    #Recorremos el string del numero...
    while(digito <= num_len-1):
    	#Si el numero siguiente es mayor que el anterior...
        if digito_1 < int(num_str[digito]):
        	#El numero no esta ordenado de mayor a menor.
            return False
        #Actualizamos valores
        digito_1 = int(num_str[digito])
        digito += 1
    #Si nunca devolvemos False, entonces el numero esta ordenao de mayor a menor.
    return True
#Prueba
print ordenado(567)
print ordenado(9876)
print ordenado(98876)

#Punto b)
def crear_password(numero):
	#Creamos dos variables para llevar los valores maximo y minimo
	num_max = -9999
	num_min = 9999
	#De nuevo, pasamos el numero a string para simplificar las cosas.
	num_str = str(numero)
	#Y obtenemos su largo
	num_len = len(num_str)
	#Comenzamos a recorrer el numero...
	digito = 0
	while (digito+2 <= num_len):
		#Obtenemos el numero compuesto por dos digitos consecutivos
		num = int(num_str[digito:digito+2])
		print digito, num
		#El numero actual es el mas grande?
		if num > num_max:
			#Actualizamos
			num_max = num
		#El numero actual es el mas chico?
		if num < num_min:
			#Actualizamos
			num_min = num
		#Actualizamos valores
		digito += 1
	#Devolvemos la contrasenna con el formato pedido
	return num_max*100+num_min
#Prueba
print crear_password(356725512199)
print crear_password(9877654)
print crear_password(123)

#Punto c)
contador_passwd = 0
contador_orden = 0
numero = raw_input("Numero: ")
while numero != "FIN":
	passwd = crear_password(int(numero))
	contador_passwd += 1
	if ordenado(passwd):
		contador_orden += 1
	numero = raw_input("Numero: ")

print "Hay", contador_passwd, "passwords"
print contador_orden, "ordenadas"
print contador_passwd - contador_orden, "no ordenadas"
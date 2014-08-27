# --- Parte 1 ---
#Pedimos el ancho y el alto
altura = int(raw_input("Altura: "))
ancho = int(raw_input("Ancho: "))

#Y dibujamos el rectangulo
for i in range(altura):
	print "*"*ancho


# --- Parte 2 ---
#Pedimos el ancho y el alto
altura = int(raw_input("Altura: "))

#Y dibujamos el triangulo
for i in range(altura+1):
	print "*"*i


# --- Parte 3 ---
#Pedimos el lado
lado = int(raw_input("Lado: "))

#Definimos una variable para dibujar los espacios
espacios = lado-1
for i in range(lado, 3*lado, 2):
	print " "*espacios + "*"*i
	espacios -= 1

espacios = 1
for i in range(3*lado-4, lado-2, -2):
	print " "*espacios + "*"*i
	espacios += 1

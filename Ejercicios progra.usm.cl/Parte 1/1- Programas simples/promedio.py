#Primero, pedimos las 4 notas
nota_1 = int(raw_input("Primera nota: "))
nota_2 = int(raw_input("Segunda nota: "))
nota_3 = int(raw_input("Tercera nota: "))
nota_4 = int(raw_input("Cuarta nota: "))

#Calculamos el promedio y lo mostramos en pantalla. Nota el decimal en el 4.0, de esa forma la division entregara numeros decimales.
promedio = (nota_1+nota_2+nota_3+nota_4)/4.0
print "El promedio es: "+str(promedio)
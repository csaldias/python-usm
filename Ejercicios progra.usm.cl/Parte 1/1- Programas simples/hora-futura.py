#Pedimos la hora actual y la cantidad de horas
hora_actual = int(raw_input("Hora actual: "))
cantidad_horas = int(raw_input("Cantidad de horas: "))

#Calculamos la hora final. Recuerda que un dia tiene 24 horas.
hora_futura = (hora_actual+cantidad_horas) % 24
print "En "+str(cantidad_horas)+" horas, el reloj marcara las "+str(hora_futura)
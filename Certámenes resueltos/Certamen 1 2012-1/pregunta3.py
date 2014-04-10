#Primero, pedimos la fecha
anno = int(raw_input("Ano: "))
mes = int(raw_input("Mes: "))
dia = int(raw_input("Dia: "))

#Ahora calculamos la edad.
#Consideraremos un año de 360 dias y meses de 30 dias, que es lo usual en progra.
#Hacemos el calculo en base a la fecha: 10 de Mayo de 2012
total_dias = (2012 - anno) * 360 + (5 - mes) * 30 + (10 - dia)
#Transformamos esto a annos, meses y dias.
anno_edad = total_dias / 360
mes_edad = (total_dias % 360) / 30
dia_edad = (total_dias % 360) % 30

print "Edad: "+str(anno_edad)+" anos, "+str(mes_edad)+" meses, "+str(dia_edad)+" dias."
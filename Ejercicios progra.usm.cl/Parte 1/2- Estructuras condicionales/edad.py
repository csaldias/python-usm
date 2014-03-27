from time import localtime

#Primero pedimos la fecha de nacimiento
print "Ingrese su fecha de nacimiento."
dia_nac = int(raw_input("Dia: "))
mes_nac = int(raw_input("Mes: "))
anno_nac = int(raw_input("Anno: "))

#Ahora obtenemos la fecha de hoy
hoy = localtime()
dia_hoy = hoy.tm_mday
mes_hoy = hoy.tm_mon
anno_hoy = hoy.tm_year

#Pasamos todo a dias, para asi obtener la edad de la persona
#Usamos la convencion de que un mes tiene 30 dias, y que un anno tiene 360 dias
dias_nac = dia_nac + mes_nac * 30 + anno_nac * 360
dias_hoy = dia_hoy + mes_hoy * 30 + anno_hoy * 360
dias_dif = dias_hoy - dias_nac
print "Usted tiene "+str(dias_dif/360)+" annos"
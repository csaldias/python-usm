#Primero, pedimos la hora
tiempo_llegada = raw_input("Ingrese hora: ")

#Ahora vemos si acaso estamos en horario normal o punta (o no opera)
if tiempo_llegada >= "06:30" and tiempo_llegada <= "22:30":
        #En operacion
	if (tiempo_llegada >= "07:30" and tiempo_llegada <= "09:00") or (tiempo_llegada >= "18:00" and tiempo_llegada <= "19:00"):
                #Hora punta
                #Trenes largos (4 vagones) y cortos (2 vagones) cada 6 minutos (en ese orden)
                print "Se encuentra en horario punta"
                
                hora_llegada = int(tiempo_llegada[:2])
                minutos_llegada = int(tiempo_llegada[3:])
                
                #Veamos que vagon llegara a la estacion y en cuanto tiempo.
                contador_largo_vagones = 0
                contador_vagones = 0 
                
                while contador_largo_vagones < minutos_llegada:
                        contador_largo_vagones += 6
                        contador_vagones += 1
                
                if contador_vagones % 2 == 0:
                        print "El tren tiene 4 vagones"
                else:
                        print "El tren tiene 2 vagones"
                
                if minutos_llegada % 6 == 0:
                        print "El tren se encuentra en el anden!"
                else:
                        print "Debe esperar "+str(6 - (minutos_llegada % 6))+" minutos"
        else:
                #Horario normal
                #Trenes largos (4 vagones) cada 12 minutos
                print "Se encuentra en horario normal"

                #Veamos en cuanto tiempo llegara el tren a la estacion.
                
                hora_llegada = int(tiempo_llegada[:2])
                minutos_llegada = int(tiempo_llegada[3:])
                print "El tren tiene 4 vagones"
                
                if minutos_llegada % 12 == 0:
                        print "El tren se encuentra en el anden!"
                else:
                        print "Debe esperar "+str(12 - (minutos_llegada % 12))+" minutos"
else:
        #El servicio no opera
        print "Ya no se encuentran trenes en este horario"

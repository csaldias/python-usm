from math import *

#Primero, pedimos la temperatura original del huevo.
t0 = float(raw_input("Ingrese la temperatura original del huevo: "))

#Ahora, establezcamos los datos.
M = 63 #Masa. Asumiremos un huevo grande
c = 3.7 #Capacidad calorifica especifica
ro = 1.038 #Densidad
K = 0.0054 #Conductividad termica
tw = 100 #Temperatura de ebullicion del agua
ty = 70 #Temperatura final

#Ahora, calculamos el tiempo necesario para llegar a la temperatura final
t = ( (M**(2/3) * c * ro**(1/3)) / (K * pi**2 * ((4 * pi)/3)**(2/3) ) * log( 0.76 * ((t0 - tw)/(ty - tw)) ))
print "El tiempo necesario es "+str(t)+" s"
#Las variables de control:
#Numero de ticket
num_ticket = 1
 
# Contadores de consultas de cada especialidad
consultas_cardiologia = 0
consultas_internista = 0
consultas_oncologia = 0
consultas_neurologia = 0
 
# Duraciones de las consultas de cada especialidad
duracion_cardio = 0
duracion_inter = 0
duracion_onco = 0
duracion_neuro = 0
 
# Hora de atencion de las distintas especialidades
hora_atencion_cardio = '08:00'
hora_atencion_onco = '08:00'
hora_atencion_inter = '08:00'
hora_atencion_neuro = '08:00'
 
 
while True: #Repetimos esta cosa de forma indefinida...
    nombre_paciente = raw_input("Paciente: ")
 
    #Si el nombre esta vacio, llegamos hasta aca
    if nombre_paciente == "": break
 
    especialidad = raw_input("Especialidad: ")
 
    print "Ticket: ", num_ticket
    num_ticket += 1
 
    if especialidad == "Cardiologia":
        #Agregamos una consulta a la cuenta
        consultas_cardiologia += 1
        print "Hora de atencion (aprox):", hora_atencion_cardio
        if hora_atencion_cardio >= '12:00': #Si la espera es muy larga...
            print "La paciencia es amarga, pero sus frutos son dulces"
 
        # Actualizamos la hora de atencion
        hora = int(hora_atencion_cardio[:2])
        minuto = int(hora_atencion_cardio[3:])
        hora += 1
        if hora < 10:
            hora_atencion_cardio = "0"+str(hora)+":"+str(minuto)
        else:
            hora_atencion_cardio = str(hora)+":"+str(minuto)
 
    # Los pasos siguientes son los mismos que en Cardiologia, pero
    # con la especialidad correspondiente.
    elif especialidad == "Internista":
        #Agregamos una consulta a la cuenta
        consultas_internista += 1
        print "Hora de atencion (aprox):", hora_atencion_inter
 
        # Actualizamos la hora de atencion
        hora = int(hora_atencion_inter[:2])
        minuto = int(hora_atencion_inter[3:])
        hora += 1
        if hora < 10:
            hora_atencion_inter = "0"+str(hora)+":"+str(minuto)
        else:
            hora_atencion_inter = str(hora)+":"+str(minuto) 
 
    if especialidad == "Oncologia":
        #Agregamos una consulta a la cuenta
        consultas_oncologia += 1
        print "Hora de atencion (aprox):", hora_atencion_onco
        
        # Actualizamos la hora de atencion
        hora = int(hora_atencion_onco[:2])
        minuto = int(hora_atencion_onco[3:])
        hora += 1
        if hora < 10:
            hora_atencion_onco = "0"+str(hora)+":"+str(minuto)
        else:
            hora_atencion_onco = str(hora)+":"+str(minuto)
    
    if especialidad == "Neurologia":
        #Agregamos una consulta a la cuenta
        consultas_neurologia += 1
        print "Hora de atencion (aprox):", hora_atencion_neuro
        
        # Actualizamos la hora de atencion
        hora = int(hora_atencion_neuro[:2])
        minuto = int(hora_atencion_neuro[3:])
        hora += 1
        if hora < 10:
            hora_atencion_neuro = "0"+str(hora)+":"+str(minuto)
        else:
            hora_atencion_neuro = str(hora)+":"+str(minuto)
 
 
# Ahora, tenemos que ver que especialidad tiene la mayor cantidad de especialistas

mayor_atencion = max(consultas_neurologia, consultas_oncologia, consultas_internista, consultas_cardiologia)
menor_atencion = min(consultas_neurologia, consultas_oncologia, consultas_internista, consultas_cardiologia)

if mayor_atencion == consultas_cardiologia: especialidad_mayor = "Cardiologia"
elif mayor_atencion == consultas_neurologia: especialidad_mayor = "Neurologia"
elif mayor_atencion == consultas_oncologia: especialidad_mayor = "Oncologia"
elif mayor_atencion == consultas_internista: especialidad_mayor = "Internista"

if menor_atencion == consultas_cardiologia:
    especialidad_menor = "Cardiologia"
    hora_menor = hora_atencion_cardio

if menor_atencion == consultas_neurologia:
    especialidad_menor = "Neurologia"
    hora_menor = hora_atencion_neuro

if menor_atencion == consultas_oncologia:
    especialidad_menor = "Oncologia"
    hora_menor = hora_atencion_onco

if menor_atencion == consultas_internista:
    especialidad_menor = "Internista"
    hora_menor = hora_atencion_inter

# Ahora, imprimimos todos los datos.
print especialidad_mayor, "es la especialidad con mas pacientes"
print especialidad_menor, "sale a las", hora_menor
alumnos = ['Pepito', 'Yayita', 'Fulanita', 'Panchito']
asistencia = [
[True, True, True, False, False, False, False],
[True, True, True, False, True,  False, True ],
[True, True, True, True,  True,  True,  True ],
[True, True, True, False, True,  True,  True ]]

#Definimos las funciones 
def total_por_alumno(tabla):
    #Variables
    asistencias = 0
    asistencia_alumnos = []
    #Recorremos la lista
    for alumno in tabla:
        for clase in alumno:
            if clase: #Si fue a clases...
                asistencias += 1 #Aumentamos el contador de asistencias.
        asistencia_alumnos.append(asistencias)
        asistencias = 0
    return asistencia_alumnos

def total_por_clase(tabla):
    #Variables
    cant_clases = len(tabla[0]) #Cuantas clases son en total?
    asistencia_clases = []
    for i in range(cant_clases): #Creamos espacio para todas las clases.
        asistencia_clases.append(0)

    for alumno in tabla:
        for clase in range(cant_clases): #Fue a la clase?
            if alumno[clase]: asistencia_clases[clase]+=1  #Sip, si fue :)
    
    return asistencia_clases
 
def alumno_estrella(tabla):
    max_asistencia = max(total_por_alumno(tabla))
    for i in range(len(alumnos)):
        if total_por_alumno(tabla)[i] == max_asistencia:
            return alumnos[i]

#Punto a)
def convertir_eeuu(nota):
    if nota >= 90: #La nota es mayor o igual a 90?
        return 'A'
    elif nota >= 70: #No se cumple lo de arriba, es menor a 90. Es mayor o igual a 70?
        return 'B'
    elif nota >= 55: #No se cumple lo de arriba, es menor a 70. Es mayor o igual a 55?
        return 'C'
    else: #No se cumple lo de arriba, es menor a 55.
        return 'F'
#Prueba
print convertir_eeuu(80)


#Punto b)
def convertir_gpa(nota):
    #El proceso es bastante simple, creo que lograras entenderlo.
    if nota == 'A':
        return 4.0
    elif nota == 'B':
        return 3.0
    elif nota == 'C':
        return 2.0
    else:
        return 0.0
#Prueba
print convertir_gpa('F')


#Punto c)
#Pedimos cada nota y la convertimos a formato EE.UU.
nota_progra = int(raw_input("Nota de Programacion: "))
eeuu_progra = convertir_eeuu(nota_progra)
print "EE.UU: ", eeuu_progra

nota_mate = int(raw_input("Nota de Matematica: "))
eeuu_mate = convertir_eeuu(nota_mate)
print "EE.UU: ", eeuu_mate

nota_fisica = int(raw_input("Nota de Fisica: "))
eeuu_fisica = convertir_eeuu(nota_fisica)
print "EE.UU: ", eeuu_fisica

#Convertimos las notas en formato EE.UU. a puntos GPA
gpa_progra = convertir_gpa(eeuu_progra)
gpa_mate = convertir_gpa(eeuu_mate)
gpa_fisica = convertir_gpa(eeuu_fisica)

#Ahora, averiguamos cuales son las dos notas mayores.
#Otra opcion podria ser usando la funcion max(), pero preferi hacerla asi.
if gpa_progra>gpa_mate and gpa_progra>gpa_fisica:
    #El GPA de Progra es el mayor de todos
    if gpa_mate>gpa_fisica:
        #El GPA de Mate es el segundo mayor
        #El orden es progra - mate - fisica
        pgpa = (gpa_progra*3+gpa_mate*5)/(3+5)
    else:
        #El GPA de Fisica es el segundo mayor
        #El orden es progra - fisica - mate
        pgpa = (gpa_progra*3+gpa_mate*3)/(3+3)
elif gpa_mate>gpa_progra and gpa_mate>gpa_fisica:
    #El GPA de Mate es el mayor de todos
    if gpa_progra>gpa_fisica:
        #El GPA de Progra es el segundo mayor
        #El orden es mate - progra - fisica
        pgpa = (gpa_mate*5+gpa_progra*3)/(5+3)
    else:
        #El GPA de Fisica es el segundo mayor
        #El orden es mate - fisica - progra
        pgpa = (gpa_mate*5+gpa_fisica*3)/(5+3)
else:
    #El GPA de Fisica es el mayor de todos
    if gpa_progra>gpa_mate:
        #El GPA de Progra es el segundo mayor
        #El orden es fisica - progra - mate
        pgpa = (gpa_fisica*3+gpa_progra*3)/(3+3)
    else:
        #El GPA de Mate es el segundo mayor
        #El orden es fisica - mate - progra
        pgpa = (gpa_fisica*3+gpa_mate*5)/(3+5)

#Y devolvemos el valor de PGPA
print "PGPA: ", pgpa
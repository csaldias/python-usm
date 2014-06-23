c = ['fulano@usm.cl', 'erika@lala.de', 'li@zi.cn', 'a@a.net',
      'gudrun@lala.de', 'otto.von.d@lorem.ipsum.de', 'org@cn.de.cl',
      'yayita@abc.cl', 'jozin@baz.cz', 'jp@foo.cl', 'dawei@hao.cn',
      'pepe@gmail.com', 'ana@usm.cl', 'polo@hotmail.com', 'fer@x.com',
      'ada@alumnos.usm.cl', 'dj@foo.cl', 'jan@baz.cz', 'd@abc.cl']
 
genericos = {'com', 'gov', 'edu', 'org', 'net', 'mil'}
 
def obtener_dominios(correos):
  #Como los dominios no se deben repetir, usamos un conjunto
  dominios = set()
  #Iteramos
  for correo in correos:
      #Desarmamos el correo y sacamos el dominio
      dominio = correo.split('@')[1]
      #Si el dominio no es generico, lo agregamos
      #Esto ultimo lo deduje del resultado, porque no
      #esta muy claro en el enunciado
      if dominio.split('.')[-1] not in genericos:
        dominios.add(dominio)
  #Transformamos el conjunto a lista
  dominios_lista = list(dominios)
  #Y la devolvemos ordenada
  return sorted(dominios_lista)

#Prueba
print obtener_dominios(c)

def contar_tld(correos):
  #Nuestro diccionario de salida
  cuenta_tld = {}
  #Iteramos
  for correo in correos:
    #Sacamos el TLD del correo
    tld = correo.split('.')[-1]
    #Si el TLD no es generico...
    if tld not in genericos:
      #Si el TLD no esta en el diccionario, lo agregamos
      if tld not in cuenta_tld:
        cuenta_tld[tld] = 1
      #Si esta, actualizamos la cuenta
      else:
        cuenta_tld[tld] += 1
  return cuenta_tld

#Prueba
print contar_tld(c)
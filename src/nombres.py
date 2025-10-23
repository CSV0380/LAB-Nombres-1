
from collections import namedtuple
import csv

FrecuenciaNombre = namedtuple('FrecuenciaNombre', 'año,nombre,frecuencia,genero')

#EJERCICIO 1
def leer_frecuencias_nombres(ruta):
    res = []
    with open(ruta, encoding= "utf-8") as f:
        lector = csv.reader(f)
        next(lector)
        for año, nombre, frecuencia, genero in lector:
            res.append(FrecuenciaNombre(int(año), nombre, int(frecuencia), genero)) 

    return res


#EJERCICIO 2
def filtrar_por_genero(lista, genero):
    res = []
    for i in lista:
        if genero.lower() == i.genero.lower():
            res.append(i)
    return res

#EJERCICIO 3
def calcular_nombres(lista, genero=None):
    res = set()
    for i in lista:
        if genero is None or genero.lower() == i.genero.lower():
            res.add(i.nombre)
    return sorted(res)


#EJERCICIO 4
def calcular_top_nombres_de_año(lista, año, n = 10, genero = None):
    res = []
    for i in lista:
        if (genero is None or genero.lower() == i.genero.lower()) and (año == i.año):
            res.append((i.nombre, i.frecuencia))
    return sorted(res, key= lambda x: x[1], reverse=True)[:n] #accedemos a frecuencia con [1] el elemento 1 de la tupla
    """ [:n] muestra los n primeros en cambio [n:] muestra los n últimos """


#EJERCICIO 5
def calcular_nombres_ambos_generos(lista):
    hombres = set()
    mujeres = set()
    for i in lista:
        if i.genero == "Hombre":
            hombres.add(i.nombre)
        elif i.genero == "Mujer":
            mujeres.add(i.nombre)
    # Intersección: nombres que están en ambos conjuntos IMPORTANTE!!!!!
    return hombres & mujeres


#EJERCICIO 6
def calcular_nombres_compuestos(lista, genero):
    res = set()
    for i in lista:
        if (genero == i.genero or genero is None) and len(i.nombre.split()) > 1: # o bien    if (genero is None or i.genero == genero) and " " in i.nombre.strip(): (strip quita todos los huecos al final y al principio de la cadena y split separa todas las palabras y las añade a una lista)
            res.add(i.nombre)
    return res


#EJERCICIO 7
def calcular_frecuencia_media_nombre_años(lista, nombre, año_i, año_f):
    res = 0
    contador = 0
    for i in lista:
        if (i.nombre == nombre.upper()) and (año_i <= i.año < año_f):
            res += i.frecuencia
            contador += 1
    if contador == 0:
        return 0
    return res/contador


#EJERCICIO 8
def calcular_nombre_mas_frecuente_año_genero(lista, año, genero):
    res = []
    for i in lista:
        if año == i.año and genero == i.genero:
            res.append((i.nombre, i.frecuencia))
    return max(res, key = lambda x : x[1])[0]


#EJERCICIO 9
def calcular_año_mas_frecuencia_nombre(lista, nombre):
    res = []
    for i in lista:
        if nombre.upper() == i.nombre.upper():
            res.append((i.frecuencia, i.año))
    return max(res, key = lambda x : x[0])[1]



if __name__ == "__main__":
    registros = leer_frecuencias_nombres("data\\frecuencias_nombres.csv")
   
    # print(f"Leídos {len(registros)} registros. Mostrando los 3 primeros {registros[:3]}")


    # genero = "Mujer"
    # print(f"Número de registros para {genero}: {len(filtrar_por_genero(registros, genero))}. Los 3 primeros son: {filtrar_por_genero(registros,genero)[:3]}")
    

    """
    if genero is None:
        print(f"Genero: 'ambos'. \fLos nombres son: \f {calcular_nombres(registros,genero)}")
    else:
        print(f"Genero: '{genero.lower()}'. \fLos nombres son: \f {calcular_nombres(registros,genero)}")
    """

    # print(f"{calcular_top_nombres_de_año(registros, 2005, 10, "Mujer")}") 


    # print(f"Los nombres de ambos generos son: {calcular_nombres_ambos_generos(registros)}") 


    # print(f"Los nombres compueston son: \f{calcular_nombres_compuestos(registros, None)}")


    # print(f"La frencuencia media es: \f{calcular_frecuencia_media_nombre_años(registros, "Francisco",2005, 2010)}")


    # print(f"El nombre más frecuente es: \f{calcular_nombre_mas_frecuente_año_genero(registros,2017, "Mujer")}")


    print(f"El año más frecuente es: \f{calcular_año_mas_frecuencia_nombre(registros, "vera")}")
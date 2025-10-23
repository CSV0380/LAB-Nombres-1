from collections import namedtuple
from matplotlib import pyplot as plt
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


#EJERCICIO 10
def calcular_año_frecuencia_por_nombre(lista, genero):
    res = dict()
    for i in lista:
            if genero == i.genero:
                if i.nombre not in res:
                    res[i.nombre] = []   # crea la lista si no existe para luego añadirle los nombres
                res[i.nombre].append((i.año, i.frecuencia))
    return res



#EJERCICIO 11
"""
def calcular_nombre_mas_frecuentes(lista, genero, decada, n):
    res = []
    for i in lista:
        if genero == i.genero and str(i.año)[2] == str(decada)[2]:
            res.append(i.nombre)
    return sorted(res[:n])


def calcular_nombre_mas_frecuentes(lista, genero, decada, n):
    res = []
    for i in lista:
        if genero == i.genero and ((i.año - 5) <= decada <= (i.año + 5)):
            res.append(i.nombre)
    return sorted(res[:n])
"""

def calcular_nombres_mas_frecuentes(lista, genero, decada, n):
    # Diccionario normal para guardar frecuencias
    frecuencias = {}
    
    # Filtramos por género y década
    for i in lista:
        if i.genero == genero and decada <= i.año <= decada + 9:
            if i.nombre in frecuencias:
                frecuencias[i.nombre] += i.frecuencia
            else:
                frecuencias[i.nombre] = i.frecuencia
    
    # Ordenamos los nombres por frecuencia de mayor a menor
    nombres_ordenados = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)
    
    # Tomamos solo los nombres y los n primeros
    return [nombre for nombre, freq in nombres_ordenados[:n]]



#EJERCICIO 12
def calcular_nombre_mas_frecuente_por_año(lista, genero):
    res = []
    años = set() #como no queremos que se repitan los años hacemos un conjunto
    for i in lista:
        if genero == i.genero:
            if i.año not in años: #comprobamos que el año no esta en la lista de años, si es que estuviera pasa al siguiente año
                res.append((i.año, i.nombre, i.frecuencia))
                años.add(i.año)

    res_ordenado = sorted(res, key=lambda x : x[0])
    return res_ordenado



#EJERCICIO 13
def calcular_frecuencia_por_año(lista, nombre):
    res = []
    años = set() #como no queremos que se repitan los años hacemos un conjunto
    for i in lista:
        if nombre == i.nombre:
            if i.año not in años: #comprobamos que el año no esta en la lista de años, si es que estuviera pasa al siguiente año
                res.append((i.año, i.frecuencia))
                años.add(i.año)

    res_ordenado = sorted(res, key=lambda x : x[0])
    return res_ordenado



#EJERCICIO 14:
def mostrar_evolucion_por_año(lista, nombre):
    registro = calcular_frecuencia_por_año(lista, nombre)
    años = [] 
    frecuencias = []
    for i in registro:
        años.append(i[0])
        frecuencias.append(i[1])
    
    plt.plot(años, frecuencias)
    plt.title("Evolución del nombre '{}'".format(nombre))
    plt.show()




#EJERCICIO 15
def calcular_frecuencias_por_nombre(lista):
    res = {}
    nombres = set()
    for i in lista:
        if i.nombre in res: # suma si ya existe
            res[i.nombre] += i.frecuencia  
        else: # inicializa si no existe
            res[i.nombre] = i.frecuencia   
    return res
    


#EJERCICIO 16
def mostrar_frecuencias_nombres(lista, n):
    res = calcular_frecuencias_por_nombre(lista)
    res_ordenado = sorted(res.items(), key=lambda x: x[1], reverse=True)[:n] #esto devuelve una lista no un diccionario
    
    nombres = [i for i, j in res_ordenado]
    frecuencias = [j for i, j in res_ordenado]

    """
    nombres = []
    frecuencias = []
    for i in res_ordenado:
        nombres.append(i[0])
        frecuencias.append(i[1])

    o bien

    for i, j in res_ordenado:
        nombres.append(i)
        frecuencias.append(j)
    """

    plt.bar(nombres, frecuencias)
    plt.xticks(rotation=80)
    plt.title("Frecuencia de los {} nombres más comunes".format(n))
    plt.show()





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


    # print(f"El año más frecuente es: \f{calcular_año_mas_frecuencia_nombre(registros, "vera")}")


    # print(f"Las frecuencias son: \f{calcular_año_frecuencia_por_nombre(registros, "Mujer")}")


    # print(f"Los nombres mas frecuentes son: \f{calcular_nombres_mas_frecuentes(registros, "Hombre", 2000, 3)}")


    # print(f"Los nombres mas frecuentes por año son: \f{calcular_nombre_mas_frecuente_por_año(registros, "Hombre")}")


    # print(f"Las frecuencias por año son: \f{calcular_frecuencia_por_año(registros, "IKER")}")


    # mostrar_evolucion_por_año(registros, "IKER")


    # print(f"Frecuencias: {calcular_frecuencias_por_nombre(registros)}")


    mostrar_frecuencias_nombres(registros, 20)
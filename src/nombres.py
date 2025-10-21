
from collections import namedtuple
import csv

FrecuenciaNombre = namedtuple('FrecuenciaNombre', 'año,nombre,frecuencia,genero')

def leer_frecuencias_nombres(ruta):
    res = []
    with open(ruta, encoding= "utf-8") as f:
        lector = csv.reader(f)
        next(lector)
        for año, nombre, frecuencia, genero in lector:
            res.append(FrecuenciaNombre(int(año), nombre, frecuencia, genero)) 

    return res



def filtrar_por_genero(lista, genero):
    res = []
    for i in lista:
        if genero.lower() == i.genero.lower():
            res.append(i)
    return res


def calcular_nombres(lista, genero=None):
    res = set()
    for i in lista:
        if genero is None or genero.lower() == i.genero.lower():
            res.add(i.nombre)
    return sorted(res)



def calcular_top_nombres_de_año(lista, año, n = 10, genero = None):
    res = []
    for i in lista:
        if (genero is None or genero.lower() == i.genero.lower()) and (año == i.año):
            res.append((i.nombre, i.frecuencia))
    return sorted(res, key= lambda x: x[1], reverse=True)[:n] #accedemos a frecuencia con [1] el elemento 1 de la tupla
    """ [:n] muestra los n primeros en cambio [n:] muestra los n últimos """



        



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

    print(f"{calcular_top_nombres_de_año(registros, 2005, 10, "Mujer")}") 
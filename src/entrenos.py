
from collections import namedtuple
import csv
from datetime import datetime

Entreno = namedtuple('Entreno', 'tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido')
result = []

def lee_entrenos(ruta_csv):
    with open(ruta_csv, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        datos = []
        for tipo, fechahora, ubicacion, duracion, \
            calorias, distancia, frecuencia,\
            compartido in lector:

            fechahora = datetime.strptime(fechahora,"%d/%m/%Y %H:%M")
            duracion=int(duracion)
            calorias=int(calorias)
            distancia=float(distancia)
            frecuencia=int(frecuencia)
            compartido= compartido =='S'


            tupla = Entreno( tipo, fechahora, ubicacion, duracion,  
                    calorias, distancia, frecuencia,
                    compartido)
            datos.append(tupla)
    return datos

def tipos_entreno(datos):
    tipos = set()
    for entreno in datos:
        tipos.add(entreno.tipo)
    return sorted(tipos)

def entrenos_duracion_superior(datos, d):
    res=[]
    for entreno in datos:
        if entreno.duracion > d:
            res.append(entreno)
    return res

def suma_calorias(datos, f_inicio, f_fin):
    suma = 0
    for entreno in datos:
        if entreno.fechahora >= f_inicio and entreno.fechahora <=f_fin:
            suma += entreno.calorias
    return suma
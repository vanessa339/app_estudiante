#Funciones del procesamiento 

import csv

def cargarEstudiantes(rutaArchivo):
    estudiantesValidos=[]

    with open(rutaArchivo, newline='', encoding='utf-8') as archivo:
        lector=csv.DictReader(archivo)
        for fila in lector:
            nombre=fila['nombre'].strip()
            try:
                nota=float(fila['nota'])
                if 0.0 <= nota <= 5.0:
                    estudiantesValidos.append({'nombre': nombre, 'nota': nota})
            except ValueError:
                pass  

    return estudiantesValidos

 
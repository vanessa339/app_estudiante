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

def mostrarEstudiantes(estudiantes):
    estudiantesOrdenados=sorted(estudiantes, key=lambda e: e['nombre'])

    print("\nEstudiantes")
    print("-" * 25)
    print(f"{'Nombre':<15} {'Nota':>5}")
    print("-" * 25)

    for est in estudiantesOrdenados:
        print(f"{est['nombre']:<15} {est['nota']:>5.2f}") 

def calcularPromedio(estudiantes):
    if not estudiantes:
        print("No hay estudiantes para calcular el promedio.")
        return

    sumaNotas=sum(e['nota'] for e in estudiantes)
    promedio=sumaNotas/len(estudiantes)
    print(f"\nPromedio general de notas: {promedio:.2f}")




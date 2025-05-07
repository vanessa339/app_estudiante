#punto de entrada del programa 
#funciones relacionadas con el registro de estudiantes 

from estudiantes.registro import cargarEstudiantes

if __name__ == "__main__":
    estudiantes = cargarEstudiantes("Estudiantes.csv")
    print(estudiantes)

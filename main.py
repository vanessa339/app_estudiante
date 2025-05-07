#punto de entrada del programa 
#funciones relacionadas con el registro de estudiantes 

from estudiantes.registro import cargarEstudiantes, mostrarEstudiantes

if __name__=="__main__":
    estudiantes=cargarEstudiantes("Estudiantes.csv")
    mostrarEstudiantes(estudiantes)

from datos import cargar_horario
from materias import registrar_materia, modificar_materia, eliminar_materia
from reportes import ver_horario, generar_reporte
from validaciones import hay_conflicto_horario

def mostrar_menu():
    print("==========================================")
    print("GENERADOR DE HORARIOS PARA ESTUDIANTES")
    print("==========================================")
    print("1. Registrar una materia o actividad")
    print("2. Ver horario semanal")
    print("3. Modificar una materia o actividad")
    print("4. Eliminar una materia o actividad")
    print("5. Generar reporte del horario")
    print("6. Salir")
    print("==========================================")

def main():
    horario = cargar_horario()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_materia(horario)
        elif opcion == "2":
            ver_horario(horario)
        elif opcion == "3":
            modificar_materia(horario)
        elif opcion == "4":
            eliminar_materia(horario)
        elif opcion == "5":
            generar_reporte(horario)
        elif opcion == "6":
            print("Gracias por utilizar el generador de horarios :)")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
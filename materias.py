from validaciones import hay_conflicto_horario
from datos import guardar_horario

def registrar_materia(horario):
    materia = input("Ingrese el nombre de la materia: ")
    dia = input("Ingrese el día de la semana: ")
    hora_inicio = pedir_hora("Ingrese la hora de inicio (Formato 24H): ")
    hora_fin = pedir_hora("Ingrese la hora de fin (Formato 24H): ")
    ubicacion = input("Ingrese la ubicación (opcional, ENTER para omitir): ")

    for evento in horario:
        if evento["dia"].lower() == dia.lower():
            if hay_conflicto_horario(hora_inicio, hora_fin, evento):
                print("No se puede registrar: hay un choque de horario.")
                return

    nuevo_evento = {
        "materia": materia, "dia": dia,
        "hora_inicio": hora_inicio, "hora_fin": hora_fin,
        "ubicacion": ubicacion
    }
    horario.append(nuevo_evento)
    guardar_horario(horario)
    print("Materia registrada correctamente.")

def modificar_materia(horario):
    nombre = input("Ingrese el nombre de la materia o actividad a modificar: ")
    for evento in horario:
        if evento["materia"].lower() == nombre.lower():
            print(f"Encontrada: {evento['dia']} {evento['hora_inicio']}-{evento['hora_fin']} en {evento['ubicacion']}")
            nuevo_dia = input("Nuevo día: ")
            nueva_hora_inicio = input("Nueva hora inicio: ")
            nueva_hora_fin = input("Nueva hora fin: ")
            nueva_ubicacion = input("Nueva ubicación (ENTER para mantener): ") or evento["ubicacion"]

            for otro in horario:
                if otro is evento:
                    continue

                if otro["dia"].lower() == nuevo_dia.lower():
                    if hay_conflicto_horario(nueva_hora_inicio, nueva_hora_fin, otro):
                        print("No se puede modificar: hay un choque de horario.")
                        return

            evento["dia"] = nuevo_dia
            evento["hora_inicio"] = nueva_hora_inicio
            evento["hora_fin"] = nueva_hora_fin
            evento["ubicacion"] = nueva_ubicacion
            guardar_horario(horario)
            print("Materia modificada correctamente.")
            return

    print("No se encontró esa materia o actividad.")

def eliminar_materia(horario):
    nombre = input("Ingrese el nombre de la materia o actividad a eliminar: ")
    dia = input("Ingrese el día en que está registrada: ")
    for evento in horario:
        if evento["materia"].lower() == nombre.lower() and evento["dia"].lower() == dia.lower():
            horario.remove(evento)
            guardar_horario(horario)
            print("Materia eliminada correctamente.")
            return
        pass
    print("No se encontró la materia en ese día.")

from validaciones import hay_conflicto_horario, hora_valida

def pedir_hora(mensaje):
    while True:
        hora = input(mensaje)
        if hora_valida(hora):
            return hora
        print("Hora inválida. Use formato HH:MM, con horas entre 00 y 23.")
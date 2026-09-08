from datetime import datetime
import json

DIAS = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
HORAS = ["06:00","07:00","08:00","09:00","10:00","11:00","12:00","13:00",
         "14:00","15:00","16:00","17:00","18:00"]

def ver_horario(horario):
    print("=================================================================")
    print(f"| {'Hora':<7} | {'Lunes':<12} | {'Martes':<12} | {'Miercoles':<12} | {'Jueves':<12} | {'Viernes':<12} |")
    print("=================================================================")

    for hora in HORAS:
        hora_actual = datetime.strptime(hora, "%H:%M")
        fila = f"| {hora:<7} |"
        for dia in DIAS:
            actividad = "-"
            for evento in horario:
                if evento["dia"].lower() == dia.lower():
                    inicio = datetime.strptime(evento["hora_inicio"], "%H:%M")
                    fin = datetime.strptime(evento["hora_fin"], "%H:%M")
                    if inicio <= hora_actual < fin:
                        actividad = evento["materia"]
            fila += f" {actividad:<12} |"
        print(fila)

    print("=================================================================")

def generar_reporte(horario):
    reporte = []
    for dia in DIAS:
        eventos_dia = []
        for evento in horario:
            if evento["dia"].lower() == dia.lower():
                eventos_dia.append(evento)
        if eventos_dia:
            reporte.append({"dia": dia, "eventos": eventos_dia})

    with open("reporte_horario.json", "w", encoding="utf-8") as archivo:
        json.dump(reporte, archivo, ensure_ascii=False, indent=4)

    contador = 0
    for bloque in reporte:
        print(f"{bloque['dia']}:")
        for evento in bloque["eventos"]:
            print(f"- {evento['materia']} ({evento['hora_inicio']}-{evento['hora_fin']}) en {evento['ubicacion']}")
            contador += 1
            if contador % 5 == 0:
                input("Presione ENTER para continuar...")

    print("Reporte guardado en reporte_horario.json")
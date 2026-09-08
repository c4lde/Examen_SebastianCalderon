import json

ARCHIVO_HORARIO = "horario.json"

def cargar_horario():
    try:
        with open(ARCHIVO_HORARIO, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

def guardar_horario(horario):
    with open(ARCHIVO_HORARIO, "w", encoding="utf-8") as archivo:
        json.dump(horario, archivo, ensure_ascii=False, indent=4)
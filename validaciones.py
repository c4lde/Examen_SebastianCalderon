from datetime import datetime

def hay_conflicto_horario(hora_inicio_nueva, hora_fin_nueva, evento_existente):
    inicio_existente = datetime.strptime(evento_existente["hora_inicio"], "%H:%M")
    fin_existente = datetime.strptime(evento_existente["hora_fin"], "%H:%M")
    inicio_nuevo = datetime.strptime(hora_inicio_nueva, "%H:%M")
    fin_nuevo = datetime.strptime(hora_fin_nueva, "%H:%M")

    return not (fin_nuevo <= inicio_existente or inicio_nuevo >= fin_existente)

def hora_valida(hora_str):
    """Verifica que el texto tenga formato HH:MM y sea una hora real (00-23)."""
    try:
        datetime.strptime(hora_str, "%H:%M")
        return True
    except ValueError:
        return False
# 📅 Generador de Horarios para Estudiantes

Sistema desarrollado en **Python** para la gestión, organización y control de horarios académicos y actividades semanales de estudiantes. Permite registrar materias, verificar conflictos de horarios, consultar la planificación semanal y generar reportes de manera sencilla.

---

## 🚀 Características Principales

- **Gestión de Materias:** Registro, modificación y eliminación de asignaturas y actividades.
- **Validación de Conflictos:** Detección automática de solapamientos o cruces en los horarios para evitar superposiciones.
- **Visualización Semanal:** Consulta clara y estructurada del horario de clases y actividades.
- **Generación de Reportes:** Creación de reportes detallados de la planificación semanal.
- **Persistencia de Datos:** Almacenamiento local mediante archivos JSON (`horario.json`).

---

## 📂 Estructura del Proyecto

El proyecto está modularizado de la siguiente manera:

```text
Proyecto/
│
├── main.py            # Punto de entrada principal y menú interactivo de la aplicación.
├── datos.py           # Gestión de carga y persistencia de datos.
├── materias.py        # Lógica para registrar, modificar y eliminar materias.
├── reportes.py        # Funciones para visualizar el horario y generar reportes.
├── validaciones.py    # Algoritmos de validación de conflictos horarios.
└── horario.json       # Archivo JSON de almacenamiento local.
```

---

## 🛠️ Requisitos Previos

- Tener instalado **Python 3.x** en tu equipo.

---

## ⚙️ Instalación y Uso

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/c4lde/Proyecto.git
   cd Proyecto
   ```

2. **Ejecutar la aplicación:**
   ```bash
   python main.py
   ```

3. **Interactuar con el sistema:**
   Sigue las opciones del menú interactivo en la terminal para gestionar tus materias y horarios.

---

## 👤 Autor

Desarrollado por [c4lde](https://github.com/c4lde).

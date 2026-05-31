# MotionLab — Análisis de Comportamiento Motor

Este repositorio corresponde al proyecto MotionLab de la materia Programación de la carrera de Ciencias del Comportamiento (Universidad de San Andrés).

El objetivo del proyecto es analizar datos simulados de una tarea motora experimental, procesando registros temporales de movimiento para calcular métricas de desempeño y generar visualizaciones.

---

# Integrantes

- Ignacio Bruzzese  
- Juan Bautista Klein Larroude
- Tobias Leonard 

---

# Contexto del problema

El comportamiento motor puede modificarse según el contexto social en el que ocurre una acción.

En este experimento, los participantes realizan movimientos repetitivos intentando alcanzar una región objetivo mientras se registra:

- posición espacial (x, y)
- tiempo transcurrido
- ocurrencia de eventos (hit)
- condición experimental

Cada participante realiza la tarea bajo una condición:

- competencia
- cooperacion

---

# Objetivos del proyecto

El sistema permite:

- cargar datos desde archivos CSV
- validar la integridad de los datos
- organizar información experimental
- calcular métricas de desempeño
- generar visualizaciones automáticas

---

# Tecnologías utilizadas

- Python
- Pandas
- Matplotlib
- OS

---

# Estructura de los datos

Cada registro contiene:

- `id_participante`
- `tiempo`
- `x`
- `y`
- `hit`
- `condicion`

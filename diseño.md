# Diseño del Sistema - MotionLab

## Descripción General

MotionLab es un sistema desarrollado para analizar datos simulados de comportamiento motor obtenidos durante tareas experimentales.

Los participantes realizan movimientos repetitivos mientras se registran variables temporales y espaciales.

El sistema procesa los datos, calcula métricas de desempeño y genera visualizaciones automáticas.

---

## Componentes

### app.py

Interfaz web desarrollada con Streamlit.

Responsabilidades:

* Carga interactiva de archivos CSV.
* Validación de datos.
* Visualización de métricas.
* Despliegue de gráficos.

### procesamiento_datos.py

Responsabilidades:

* Filtrado de datos por participante.
* Generación de gráficos individuales.

Funciones principales:

* filtrar_por_participante()
* graficar_participante()

### metricas.py

Responsabilidades:

* Generación de gráficos generales.
* Comparación de desempeño.

Funciones principales:

* generar_graficos()

---

## Flujo General

1. Usuario carga archivo CSV.
2. Se verifica la estructura del dataset.
3. Se calculan indicadores generales.
4. Se generan gráficos globales.
5. Se selecciona un participante.
6. Se generan gráficos individuales.
7. Se muestran resultados en pantalla.

---

## Datos Esperados

El sistema espera las siguientes columnas:

* timestamp
* condicion
* hit_A
* hit_B
* hits_total
* x_A
* x_B
* activity_roi_A
* activity_roi_B

---

## Salidas

El sistema genera:

* Indicadores clave (KPIs).
* Gráfico temporal de hits.
* Comparación de hits por participante.
* Actividad ROI por participante.
* Distribución de posición X por participante.

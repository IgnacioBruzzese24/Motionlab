import streamlit as st
import pandas as pd
import os

from metricas import generar_graficos
from procesamiento_datos import graficar_participante

st.set_page_config(
page_title="MotionLab",
page_icon="📊",
layout="wide"
)

st.title("📊 MotionLab — Análisis de Comportamiento Motor")

st.markdown("""
Esta aplicación permite cargar datos experimentales,
validarlos, calcular métricas de desempeño y visualizar
gráficos del comportamiento motor.
""")

archivo = st.file_uploader(
"Seleccione un archivo CSV",
type=["csv"]
)

if archivo is not None:

```
try:

    df = pd.read_csv(archivo)

    columnas_obligatorias = [
        "timestamp",
        "condicion",
        "hit_A",
        "hit_B",
        "hits_total",
        "x_A",
        "x_B",
        "activity_roi_A",
        "activity_roi_B"
    ]

    faltantes = [
        col
        for col in columnas_obligatorias
        if col not in df.columns
    ]

    if faltantes:
        raise ValueError(
            f"Faltan columnas obligatorias: {', '.join(faltantes)}"
        )

except ValueError as e:

    st.error(str(e))
    st.stop()

except Exception as e:

    st.error(f"Error al procesar el archivo: {e}")
    st.stop()

st.success("Archivo cargado correctamente")

st.header("Indicadores Clave")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Registros",
        len(df)
    )

with col2:
    st.metric(
        "Hits Totales",
        int(df["hits_total"].max())
    )

with col3:
    st.metric(
        "Hits Participante A",
        int(df["hit_A"].sum())
    )

with col4:
    st.metric(
        "Hits Participante B",
        int(df["hit_B"].sum())
    )

generar_graficos(df)

st.header("Gráficos Generales")

if os.path.exists(
    "graficos/evolucion_hits_temporal.png"
):
    st.image(
        "graficos/evolucion_hits_temporal.png",
        caption="Evolución temporal de hits"
    )

if os.path.exists(
    "graficos/comparacion_hits_participantes.png"
):
    st.image(
        "graficos/comparacion_hits_participantes.png",
        caption="Comparación de hits por participante"
    )

st.header("Análisis por Participante")

participante = st.selectbox(
    "Seleccione un participante",
    ["A", "B"]
)

try:

    graficar_participante(
        df,
        participante
    )

    actividad = (
        f"graficos/actividad_roi_{participante}.png"
    )

    distribucion = (
        f"graficos/distribucion_x_{participante}.png"
    )

    if os.path.exists(actividad):
        st.image(
            actividad,
            caption=f"Actividad ROI Participante {participante}"
        )

    if os.path.exists(distribucion):
        st.image(
            distribucion,
            caption=f"Distribución X Participante {participante}"
        )

except Exception as e:

    st.error(
        f"No fue posible generar los gráficos: {e}"
    )
```

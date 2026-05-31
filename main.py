# -*- coding: utf-8 -*-
"""
Created on Sun May 31 19:54:39 2026

@author: nacho
"""

import os
import matplotlib.pyplot as plt

from procesamiento_datos import cargar_datos
from metricas import calcular_hit_totales, calcular_tiempo_primer_hit, hits_por_condicion

ruta = "MotionLab_mock_data.csv"

df = cargar_datos(ruta)



id_usuario = int(
    input(
        "Ingrese participante: "
    )
)

participante = df[
    df["id_participante"] ==
    id_usuario
]

if participante.empty:

    raise ValueError(
        "Participante inexistente"
    )



hits = calcular_hits_totales(
    participante
)

primer_hit = calcular_tiempo_primer_hit(
    participante
)

print(
    "Hits:",
    hits
)

print(
    "Primer hit:",
    primer_hit
)



if not os.path.exists(
    "graficos"
):

    os.mkdir(
        "graficos"
    )



agrupado = df.groupby(
    "condicion"
)["hit"].sum()

plt.figure(
    figsize=(8,5)
)

agrupado.plot(
    kind="bar"
)

plt.title(
    "Hits por condición"
)

plt.ylabel(
    "Hits"
)

plt.tight_layout()

plt.savefig(
    "graficos/hits_condicion.png"
)

plt.close()



plt.figure(
    figsize=(10,5)
)

participante.plot(
    x="tiempo",
    y="x",
    kind="line"
)

plt.title(
    "Posición X en el tiempo"
)

plt.tight_layout()

plt.savefig(
    "graficos/evolucion_temporal.png"
)

plt.close()
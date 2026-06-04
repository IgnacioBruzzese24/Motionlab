# -*- coding: utf-8 -*-
"""
Created on Sun May 31 19:54:39 2026

@author: nacho
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

ruta = "MotionLab_mock_data.csv"

# Cargar datos asignando nombres de columnas manualmente
# Según la estructura: id_participante, tiempo, x, y, hit, condicion
df = pd.read_csv(
    ruta, 
    names=["id_participante", "tiempo", "x", "y", "hit", "condicion"]
)

print("Columnas del archivo:", df.columns.tolist())
print("\nPrimeras filas:")
print(df.head())

id_usuario = int(
    input(
        "\nIngrese participante: "
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

# Calcular hits totales
hits = participante["hit"].sum()

# Calcular tiempo del primer hit
primeros_hits = participante[participante["hit"] == True]
if not primeros_hits.empty:
    primer_hit = primeros_hits["tiempo"].iloc[0]
else:
    primer_hit = -1

print(
    "\nHits:",
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

# Hits por condición
agrupado = df.groupby("condicion")["hit"].sum()

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

print("\n✅ Gráficos guardados en la carpeta 'graficos/'")

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 15:21:16 2026
@author: nacho
"""
import os
import pandas as pd
import matplotlib.pyplot as plt


def filtrar_por_participante(df: pd.DataFrame, participante: str) -> pd.DataFrame:
    """
    Devuelve las columnas correspondientes a un participante específico
    utilizando selección vectorizada de Pandas.

    Parámetros:
        df (pd.DataFrame): DataFrame completo con los datos del experimento.
        participante (str): Letra del participante ('A' o 'B').

    Retorna:
        pd.DataFrame: subconjunto de columnas del participante
                      junto con timestamp y condicion,
                      o None si el participante no existe.
    """
    columnas = [col for col in df.columns if col.endswith(f"_{participante}")]
    if not columnas:
        return None
    return df[["timestamp", "condicion"] + columnas]


def graficar_participante(df: pd.DataFrame, participante: str, carpeta: str = "graficos") -> None:
    """
    Genera y guarda los gráficos de un participante específico.

    Parámetros:
        df (pd.DataFrame): DataFrame completo con los datos del experimento.
        participante (str): Letra del participante ('A' o 'B').
        carpeta (str): Carpeta destino de los gráficos. Por defecto: 'graficos'.

    Retorna:
        None
    """
    os.makedirs(carpeta, exist_ok=True)

    df_p = filtrar_por_participante(df, participante)
    if df_p is None:
        raise ValueError(f"Participante '{participante}' no encontrado en el DataFrame.")

    # --- Gráfico 1: Línea temporal de actividad en ROI ---
    plt.figure(figsize=(11, 5))
    df_p.plot(
        kind="line",
        x="timestamp",
        y=f"activity_roi_{participante}",
        color="#b45309",
        linewidth=1.5,
        ax=plt.gca()
    )
    plt.title(f"Actividad en ROI - Participante {participante}",
              fontsize=13, fontweight="bold", pad=15)
    plt.xlabel("Tiempo (segundos)", fontsize=11)
    plt.ylabel("Actividad en ROI (True/False)", fontsize=11)
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.tight_layout()
    plt.savefig(f"{carpeta}/actividad_roi_{participante}.png", dpi=300)
    plt.close()

    # --- Gráfico 2: Boxplot de posición X del participante ---
    plt.figure(figsize=(7, 5))
    df_p[f"x_{participante}"].dropna().plot(
        kind="box",
        vert=True,
        patch_artist=True,
        boxprops=dict(facecolor="#cbd5e1", color="#0f172a")
    )
    plt.title(f"Distribución de Posición X - Participante {participante}",
              fontsize=13, fontweight="bold", pad=15)
    plt.ylabel("Posición X", fontsize=11)
    plt.grid(True, linestyle="--", alpha=0.4, axis="y")
    plt.tight_layout()
    plt.savefig(f"{carpeta}/distribucion_x_{participante}.png", dpi=300)
    plt.close()
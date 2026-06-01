import os
import pandas as pd
import matplotlib.pyplot as plt


def generar_graficos(df: pd.DataFrame, carpeta: str = "graficos") -> None:
    """
    Genera y guarda los gráficos de análisis del experimento de salto.
    Crea automáticamente la carpeta de destino si no existe.

    Parámetros:
        df (pd.DataFrame): DataFrame con los datos del experimento.
                           Debe contener las columnas: 'timestamp',
                           'hits_total', 'hit_A', 'hit_B'.
        carpeta (str): Ruta de la carpeta donde se guardarán los gráficos.
                       Por defecto: 'graficos'.

    Retorna:
        None
    """
    os.makedirs(carpeta, exist_ok=True)

    # --- Gráfico 1: Línea temporal de hits acumulados ---
    plt.figure(figsize=(11, 5))
    df.plot(
        kind="line",
        x="timestamp",
        y="hits_total",
        color="#b45309",
        linewidth=1.5,
        ax=plt.gca()
    )
    plt.title("Evolución de Hits Acumulados a lo Largo del Tiempo",
              fontsize=13, fontweight="bold", pad=15)
    plt.xlabel("Tiempo (segundos)", fontsize=11)
    plt.ylabel("Hits Acumulados", fontsize=11)
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.tight_layout()
    plt.savefig(f"{carpeta}/evolucion_hits_temporal.png", dpi=300)
    plt.close()

    # --- Gráfico 2: Barras comparativas de hits por participante ---
    hits_por_participante = pd.Series({
        "Participante A": df["hit_A"].sum(),
        "Participante B": df["hit_B"].sum()
    })
    plt.figure(figsize=(7, 5))
    hits_por_participante.plot(
        kind="bar",
        color="#1e3a8a",
        edgecolor="black",
        alpha=0.8
    )
    plt.title("Comparación de Hits Totales por Participante",
              fontsize=13, fontweight="bold", pad=15)
    plt.xlabel("Participante", fontsize=11)
    plt.ylabel("Cantidad de Hits", fontsize=11)
    plt.xticks(rotation=0)
    plt.grid(True, linestyle="--", alpha=0.5, axis="y")
    plt.tight_layout()
    plt.savefig(f"{carpeta}/comparacion_hits_participantes.png", dpi=300)
    plt.close()
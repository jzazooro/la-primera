import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Ruta relativa al archivo CSV desde la ubicación de analisis.py
ruta_csv = "DATOS/datos22-23.csv"
# Leer el archivo CSV
df = pd.read_csv(ruta_csv)
# Corrigiendo los nombres de las columnas eliminando espacios extras
df.columns = df.columns.str.strip()


### PARTIDOS CON GOLES DE AMBOS EQUIPOS VS. PARTIDOS SIN GOLES DE AMBOS EQUIPOS EN TODA LA COMPETICIÓN
# Revisando las condiciones correctamente
partidos_con_goles_ambos_correcto = df[(df['resultadoparte1'] > 0) & (df['resutadoparte2'] > 0)]
partidos_sin_goles_ambos_correcto = df[~((df['resultadoparte1'] > 0) & (df['resutadoparte2'] > 0))]
# Contando los partidos bajo las condiciones corregidas
num_partidos_con_goles_ambos_correcto = len(partidos_con_goles_ambos_correcto)
num_partidos_sin_goles_ambos_correcto = len(partidos_sin_goles_ambos_correcto)
# Datos para el diagrama corregido
datos_partidos_correcto = [num_partidos_con_goles_ambos_correcto, num_partidos_sin_goles_ambos_correcto]
etiquetas_partidos_correcto = ['Partidos con Goles de Ambos', 'Partidos sin Goles de Ambos']
# Creando el diagrama corregido
plt.figure(figsize=(8, 6))
plt.bar(etiquetas_partidos_correcto, datos_partidos_correcto, color=['green', 'orange'])
plt.title('Comparación de Partidos: Goles de Ambos Equipos vs. No Goles de Ambos')
plt.ylabel('Número de Partidos')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

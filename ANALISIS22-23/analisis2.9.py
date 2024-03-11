import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Ruta relativa al archivo CSV desde la ubicación de analisis.py
ruta_csv = "DATOS/datos22-23.csv"
# Leer el archivo CSV
df = pd.read_csv(ruta_csv)
# Corrigiendo los nombres de las columnas eliminando espacios extras
df.columns = df.columns.str.strip()

### DIAGRAMA DE GOLES MARCADOS EN CASA VS VISITANTE EN FASE DE GRUPOS
# Asegurándose de que los nombres de las columnas se manejan correctamente
df.columns = df.columns.str.strip()
# Filtrando los datos para incluir solo la fase de grupos, si es necesario
fase_grupos = df[df['fase'] == 'Fase de Grupos']
# Calculando goles marcados como local y visitante
goles_marcados_local = df.groupby('equipo1')['resultadoparte1'].sum().add(df.groupby('equipo1')['resutadoparte2'].sum(), fill_value=0)
goles_marcados_visitante = df.groupby('equipo2')['resutadoparte2'].sum()
# Asegurando que ambos tengan el mismo índice para poder comparar
goles_marcados_local = goles_marcados_local.reindex(goles_marcados_local.index.union(goles_marcados_visitante.index), fill_value=0)
goles_marcados_visitante = goles_marcados_visitante.reindex(goles_marcados_visitante.index.union(goles_marcados_local.index), fill_value=0)
# Preparando los datos para el Box Plot
data = [goles_marcados_local, goles_marcados_visitante]
# Creando el Box Plot
plt.figure(figsize=(10, 6))
plt.boxplot(data, patch_artist=True, labels=['Goles Marcados en Casa', 'Goles Marcados como Visitante'])
plt.title('Distribución de Goles Marcados en Casa vs Visitante')
plt.ylabel('Goles Marcados')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

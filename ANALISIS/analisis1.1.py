import pandas as pd
import matplotlib.pyplot as plt

# Ruta relativa al archivo CSV desde la ubicación de analisis.py
ruta_csv = "DATOS/datos22-23.csv"
# Leer el archivo CSV
df = pd.read_csv(ruta_csv)
# Corrigiendo los nombres de las columnas eliminando espacios extras
df.columns = df.columns.str.strip()

# Filtrando datos para incluir solo la fase de grupos
fase_grupos = df[df['fase'] == 'Fase de Grupos']

### EQUIPOS QUE MAS PUNTOS OBTIENEN EN FASE DE GRUPOS
# Sumando los puntos de cada equipo, corrigiendo el nombre de las columnas
puntos_equipos = fase_grupos.groupby('equipo1')['puntosequipo1'].sum().add(fase_grupos.groupby('equipo2')['puntosequipo2'].sum(), fill_value=0)
# Ordenando los equipos por puntos obtenidos
puntos_equipos_sorted = puntos_equipos.sort_values(ascending=False)
# Creando el gráfico de barras con los nombres corregidos
plt.figure(figsize=(10, 8))
puntos_equipos_sorted.plot(kind='bar')
plt.title('Puntos Obtenidos por Equipo en la Fase de Grupos - Champions League')
plt.xlabel('Equipo')
plt.ylabel('Puntos Totales')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

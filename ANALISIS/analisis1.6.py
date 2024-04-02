import pandas as pd
import matplotlib.pyplot as plt

# Ruta relativa al archivo CSV desde la ubicación de analisis.py
ruta_csv = "DATOS/datos21-22.csv"
# Leer el archivo CSV
df = pd.read_csv(ruta_csv)
# Corrigiendo los nombres de las columnas eliminando espacios extras
df.columns = df.columns.str.strip()

# Filtrando datos para incluir solo la fase de grupos
fase_grupos = df[df['fase'] == 'Fase de Grupos']

### puntos obtenidos de local
# Sumando los puntos obtenidos por cada equipo como local
puntos_obtenidos_local = fase_grupos.groupby('equipo1')['puntosequipo1'].sum()
# Ordenando los equipos por puntos obtenidos como local
puntos_obtenidos_local_sorted = puntos_obtenidos_local.sort_values(ascending=False)
# Creando el gráfico de barras para los puntos obtenidos como local
plt.figure(figsize=(10, 8))
puntos_obtenidos_local_sorted.plot(kind='bar', color='red')
plt.title('Puntos Obtenidos por Equipo de Local en la Fase de Grupos - Champions League')
plt.xlabel('Equipo')
plt.ylabel('Puntos Totales Obtenidos de Local')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
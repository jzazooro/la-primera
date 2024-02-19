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

### puntos obtenidos de visitante
# Sumando los puntos obtenidos por cada equipo como visitante
puntos_obtenidos_visitante = fase_grupos.groupby('equipo2')['puntosequipo2'].sum()
# Ordenando los equipos por puntos obtenidos como visitante
puntos_obtenidos_visitante_sorted = puntos_obtenidos_visitante.sort_values(ascending=False)
# Creando el gráfico de barras para los puntos obtenidos como visitante
plt.figure(figsize=(10, 8))
puntos_obtenidos_visitante_sorted.plot(kind='bar', color='cyan')
plt.title('Puntos Obtenidos de Visitante por Equipo en la Fase de Grupos - Champions League')
plt.xlabel('Equipo')
plt.ylabel('Puntos Totales Obtenidos de Visitante')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
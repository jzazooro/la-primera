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

### EQUIPOS QUE MAS GOLES MARCAN DE VISITANTE
# Calculando los goles marcados como visitante (equipo2) utilizando solo la columna 'resutadoparte2'
goles_marcados_visitante_p2 = fase_grupos.groupby('equipo2')['resutadoparte2'].sum()
# Ordenando los equipos por goles marcados como visitante en la segunda parte
goles_marcados_visitante_p2_sorted = goles_marcados_visitante_p2.sort_values(ascending=False)
# Creando el gráfico de barras para los goles marcados como visitante en la segunda parte
plt.figure(figsize=(10, 8))
goles_marcados_visitante_p2_sorted.plot(kind='bar', color='blue')
plt.title('Goles Marcados por Equipo de Visitante en la Fase de Grupos - Champions League')
plt.xlabel('Equipo')
plt.ylabel('Goles Totales Marcados de Visitante (2ª Parte)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
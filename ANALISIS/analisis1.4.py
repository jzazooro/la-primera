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

### EQUIPOS QUE MAS GOLES MARCAN DE LOCAL
# Generando un gráfico basado únicamente en los goles marcados en la columna 'resultadoparte1' para los equipos cuando juegan de local (equipo1)
# Calculando los goles marcados de local utilizando solo la columna 'resultadoparte1'
goles_marcados_local_p1 = fase_grupos.groupby('equipo1')['resultadoparte1'].sum()
# Ordenando los equipos por goles marcados de local en la primera parte
goles_marcados_local_p1_sorted = goles_marcados_local_p1.sort_values(ascending=False)
# Creando el gráfico de barras para los goles marcados de local en la primera parte
plt.figure(figsize=(10, 8))
goles_marcados_local_p1_sorted.plot(kind='bar', color='purple')
plt.title('Goles Marcados por Equipo de Local en la Fase de Grupos - Champions League')
plt.xlabel('Equipo')
plt.ylabel('Goles Totales Marcados de Local (1ª Parte)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
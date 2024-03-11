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

### EQUIPOS QUE MAS GOLES MARCAN EN FASE DE GRUPOS
# Sumando los goles marcados por cada equipo tanto como 'equipo1' como 'equipo2'
goles_equipos = fase_grupos.groupby('equipo1')['resultadoparte1'].sum().add(fase_grupos.groupby('equipo1')['resutadoparte2'].sum(), fill_value=0).add(fase_grupos.groupby('equipo2')['resutadoparte2'].sum(), fill_value=0)
# Ordenando los equipos por goles marcados
goles_equipos_sorted = goles_equipos.sort_values(ascending=False)
# Creando el gráfico de barras para los goles marcados
plt.figure(figsize=(10, 8))
goles_equipos_sorted.plot(kind='bar')
plt.title('Goles Marcados por Equipo en la Fase de Grupos - Champions League')
plt.xlabel('Equipo')
plt.ylabel('Goles Totales')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
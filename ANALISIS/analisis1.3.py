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

### EQUIPOS QUE MAS GOLES RECIBEN EN FASE DE GRUPOS
# Calculating goals conceded when playing as team1
goles_recibidos_equipo1 = fase_grupos.groupby('equipo1')['resutadoparte2'].sum()
# Calculating goals conceded when playing as team2
goles_recibidos_equipo2 = fase_grupos.groupby('equipo2')['resultadoparte1'].sum()
# Summing both to get total goals conceded by each team
goles_recibidos = goles_recibidos_equipo1.add(goles_recibidos_equipo2, fill_value=0)
# Sorting teams by goals conceded
goles_recibidos_sorted = goles_recibidos.sort_values(ascending=False)
# Eliminando la barra más pequeña del gráfico (equipo con menos goles recibidos)
goles_recibidos_sorted_modificado = goles_recibidos_sorted[:-1]
# Creando el gráfico de barras modificado
plt.figure(figsize=(10, 8))
goles_recibidos_sorted_modificado.plot(kind='bar', color='tomato')
plt.title('Goles Recibidos por Equipo en la Fase de Grupos - Champions League')
plt.xlabel('Equipo')
plt.ylabel('Goles Totales Recibidos')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
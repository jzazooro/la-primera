import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Ruta relativa al archivo CSV desde la ubicación de analisis.py
ruta_csv = "DATOS/datos21-22.csv"
# Leer el archivo CSV
df = pd.read_csv(ruta_csv)
# Corrigiendo los nombres de las columnas eliminando espacios extras
df.columns = df.columns.str.strip()

# Filtrando datos para incluir solo la fase de grupos
fase_grupos = df[df['fase'] == 'Fase de Grupos']

### ANALISIS BARCELONA FASE DE GRUPOS
# Suma de goles marcados como local por cada equipo
goles_marcados_local = fase_grupos.groupby('equipo1')['resultadoparte1'].sum().add(fase_grupos.groupby('equipo1')['resutadoparte2'].sum(), fill_value=0)
# Suma de goles recibidos como visitante por cada equipo
goles_recibidos_visitante = fase_grupos.groupby('equipo2')['resultadoparte1'].sum()
# Suma de puntos obtenidos como local por cada equipo
puntos_obtenidos_local = fase_grupos.groupby('equipo1')['puntosequipo1'].sum()
# Suma de puntos obtenidos como visitante por cada equipo
puntos_obtenidos_visitante = fase_grupos.groupby('equipo2')['puntosequipo2'].sum()
# Seleccionando los primeros 3 equipos como ejemplo para el gráfico de radar
equipos_seleccionados = goles_marcados_local.nlargest(1).index.tolist()
# Preparando los datos para el gráfico de radar
datos_radar = []
for equipo in equipos_seleccionados:
    datos_equipo = [
        goles_marcados_local.get(equipo, 0),
        goles_recibidos_visitante.get(equipo, 0),
        puntos_obtenidos_local.get(equipo, 0),
        puntos_obtenidos_visitante.get(equipo, 0)
    ]
    datos_radar.append(datos_equipo)
# Métricas para el gráfico de radar
metricas_radar = ['Goles Marcados Local', 'Goles Recibidos Visitante', 'Puntos Local', 'Puntos Visitante']
# Convertir los datos a un array para facilitar su manejo
datos_radar = np.array(datos_radar)
# Número de métricas
num_vars = len(metricas_radar)
# Ángulos para cada eje en el gráfico de radar
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
# El gráfico de radar necesita ser circular, así que necesitamos completar la circunferencia
datos_radar = np.concatenate((datos_radar, datos_radar[:,[0]]), axis=1)
angles += angles[:1]
# Dibujando el gráfico de radar con los datos calculados
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
for i, equipo in enumerate(equipos_seleccionados):
    ax.plot(angles, datos_radar[i], label=equipo)
    ax.fill(angles, datos_radar[i], alpha=0.25)
# Etiquetas para cada métrica
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(metricas_radar)
# Leyenda
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))
plt.show()

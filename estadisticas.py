import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Cargando los datos desde el archivo subido
df = pd.read_csv('datos22-23.csv')
# Corrigiendo los nombres de las columnas eliminando espacios extras
df.columns = df.columns.str.strip()

### MEDIA DE GOLES EN LOS PARTIDOS DE LA COMPETICION
# Sumando todos los goles marcados en la competición
total_goles_competicion = df['resultadoparte1'].sum() + df['resutadoparte2'].sum()
# Contando el número total de partidos en la competición
num_total_partidos_competicion = len(df)
# Calculando la media de goles por partido en toda la competición
media_goles_competicion = total_goles_competicion / num_total_partidos_competicion
print("la media de goles en los partidos de la competicion es: ", media_goles_competicion)

### CORRELACION ENTRE GOLES MARCADOS Y PUNTOS OBTENIDOS
df['goles_marcados'] = df['resultadoparte1'] + df['resutadoparte2']
df_equipo1 = df[['equipo1', 'puntosequipo1', 'goles_marcados']].rename(columns={'equipo1': 'equipo', 'puntosequipo1': 'puntos'})
df_equipo2 = df[['equipo2', 'puntosequipo2', 'goles_marcados']].rename(columns={'equipo2': 'equipo', 'puntosequipo2': 'puntos'})
# Combinando los datos duplicados
df_combinado = pd.concat([df_equipo1, df_equipo2], ignore_index=True)
# Calculando la correlación entre goles marcados y puntos obtenidos
correlacion = df_combinado['goles_marcados'].corr(df_combinado['puntos'])
print("La correlacion entre los goles marcados y los puntos obtenidos es de: ", correlacion)

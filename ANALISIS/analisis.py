import pandas as pd
import matplotlib.pyplot as plt

# Cargando los datos desde el archivo subido
df = pd.read_csv('datos22-23.csv')
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

### EQUIPOS QUE MAS GOLES MARCAN DE LOCAL
# Generando un gráfico basado únicamente en los goles marcados en la columna 'resultadoparte1' para los equipos cuando juegan de local (equipo1)
# Calculando los goles marcados de local utilizando solo la columna 'resultadoparte1'
goles_marcados_local_p1 = fase_grupos.groupby('equipo1')['resultadoparte1'].sum()
# Ordenando los equipos por goles marcados de local en la primera parte
goles_marcados_local_p1_sorted = goles_marcados_local_p1.sort_values(ascending=False)
# Creando el gráfico de barras para los goles marcados de local en la primera parte
plt.figure(figsize=(10, 8))
goles_marcados_local_p1_sorted.plot(kind='bar', color='purple')
plt.title('Goles Marcados de Local por Equipo - Fase de Grupos Champions League')
plt.xlabel('Equipo')
plt.ylabel('Goles Totales Marcados de Local (1ª Parte)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

### EQUIPOS QUE MAS GOLES MARCAN DE VISITANTE
# Calculando los goles marcados como visitante (equipo2) utilizando solo la columna 'resutadoparte2'
goles_marcados_visitante_p2 = fase_grupos.groupby('equipo2')['resutadoparte2'].sum()
# Ordenando los equipos por goles marcados como visitante en la segunda parte
goles_marcados_visitante_p2_sorted = goles_marcados_visitante_p2.sort_values(ascending=False)
# Creando el gráfico de barras para los goles marcados como visitante en la segunda parte
plt.figure(figsize=(10, 8))
goles_marcados_visitante_p2_sorted.plot(kind='bar', color='blue')
plt.title('Goles Marcados de Visitante por Equipo - Fase de Grupos Champions League')
plt.xlabel('Equipo')
plt.ylabel('Goles Totales Marcados de Visitante (2ª Parte)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

### puntos obtenidos de local
# Sumando los puntos obtenidos por cada equipo como local
puntos_obtenidos_local = fase_grupos.groupby('equipo1')['puntosequipo1'].sum()
# Ordenando los equipos por puntos obtenidos como local
puntos_obtenidos_local_sorted = puntos_obtenidos_local.sort_values(ascending=False)
# Creando el gráfico de barras para los puntos obtenidos como local
plt.figure(figsize=(10, 8))
puntos_obtenidos_local_sorted.plot(kind='bar', color='red')
plt.title('Puntos Obtenidos de Local por Equipo en la Fase de Grupos - Champions League')
plt.xlabel('Equipo')
plt.ylabel('Puntos Totales Obtenidos de Local')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

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

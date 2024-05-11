import pandas as pd

file_path = r'DATOS/actualidad.csv'
data = pd.read_csv(file_path)

data.head()

# Limpiar los nombres de las columnas (eliminar espacios adicionales)
data.columns = data.columns.str.strip()

# Crear un score basado en las estadísticas disponibles
# Vamos a considerar más positivo tener mayor posesión, mejor precisión de pases, más goles a favor, menos goles en contra, y más tiros a puerta. Las tarjetas se considerarán negativamente.

import numpy as np

# Generar enfrentamientos aleatorios
np.random.seed(42)  # Para reproducibilidad
n_matches = 100  # Número de partidos a simular

# Elegir equipos aleatoriamente para los partidos
home_teams = np.random.choice(data['equipo'], n_matches, replace=True)
away_teams = np.random.choice(data['equipo'], n_matches, replace=True)

# Crear un DataFrame para los enfrentamientos
matches = pd.DataFrame({
    'HomeTeam': home_teams,
    'AwayTeam': away_teams
})

# Unir las estadísticas de los equipos para cada partido
matches_stats = matches.merge(data, left_on='HomeTeam', right_on='equipo', suffixes=('', '_home'))
matches_stats = matches_stats.merge(data, left_on='AwayTeam', right_on='equipo', suffixes=('_home', '_away'))

# Eliminar las columnas redundantes
matches_stats.drop(columns=['equipo_home', 'equipo_away'], inplace=True)

matches_stats.head()

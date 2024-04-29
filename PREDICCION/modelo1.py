import pandas as pd

file_path = 'actualidad.csv'
data = pd.read_csv(file_path)

data.head()

# Limpiar los nombres de las columnas (eliminar espacios adicionales)
data.columns = data.columns.str.strip()

# Crear un score basado en las estadísticas disponibles
# Vamos a considerar más positivo tener mayor posesión, mejor precisión de pases, más goles a favor, menos goles en contra, y más tiros a puerta. Las tarjetas se considerarán negativamente.

weights = {
    'partidos jugados': 0,  # Este valor no influye directamente, más bien normalizaremos otras estadísticas con este
    'porcentaje posesion': 0.2,
    'porcentaje pases acertados': 0.1,
    'asistencias de gol': 0.2,
    'goles a favor': 0.3,
    'goles en contra': -0.2,
    'tiros a puerta': 0.2,
    'corners': 0.05,
    'tarjetas amarillas': -0.05,
    'tarjetas rojas': -0.1
}

# Calculamos el score para cada equipo normalizando algunas estadísticas por partidos jugados
data['score'] = (
    data['porcentaje posesion'] * weights['porcentaje posesion'] +
    data['porcentaje pases acertados'] * weights['porcentaje pases acertados'] +
    (data['asistencias de gol'] / data['partidos jugados']) * weights['asistencias de gol'] +
    (data['goles a favor'] / data['partidos jugados']) * weights['goles a favor'] +
    (data['goles en contra'] / data['partidos jugados']) * weights['goles en contra'] +
    (data['tiros a puerta'] / data['partidos jugados']) * weights['tiros a puerta'] +
    (data['corners'] / data['partidos jugados']) * weights['corners'] +
    (data['tarjetas amarillas'] / data['partidos jugados']) * weights['tarjetas amarillas'] +
    (data['tarjetas rojas'] / data['partidos jugados']) * weights['tarjetas rojas']
)

# Verificar los scores y el dataframe final
data[['equipo', 'score']].sort_values(by='score', ascending=False)

def predict_winner(team1, team2, data):
    if team1 not in data['equipo'].values or team2 not in data['equipo'].values:
        return "Uno o ambos de los equipos no se encuentran en la base de datos."
    
    team1_score = data.loc[data['equipo'] == team1, 'score'].values[0]
    team2_score = data.loc[data['equipo'] == team2, 'score'].values[0]
    
    if team1_score > team2_score:
        print(f"El ganador predicho es: {team1}")
    elif team2_score > team1_score:
        print(f"El ganador predicho es: {team2}")
    else:
        print(f"El partido podría terminar en empate según las estadísticas.")

# pide al usuario que introduzca los equipos
equipo1 = input("Introduce el nombre del primer equipo: ")
equipo2 = input("Introduce el nombre del segundo equipo: ")

# Ejemplo de predicción entre dos equipos
predict_winner(equipo1, equipo2, data)
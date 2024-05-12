import pandas as pd
import csv

file_path = r'DATOS/actualidad.csv'
data = pd.read_csv(file_path)

data.head()

# Limpiar los nombres de las columnas (eliminar espacios adicionales)
data.columns = data.columns.str.strip()

equipos = []

with open(file_path, 'r', newline='') as archivo:
    lector_csv = csv.reader(archivo)
    for fila in lector_csv:
        if fila:  # Verificar si la fila no está vacía
            primer_elemento = fila[0]
            equipos.append(primer_elemento)

# Crear un score basado en las estadísticas disponibles
# Vamos a considerar más positivo tener mayor posesión, mejor precisión de pases, más goles a favor, menos goles en contra, y más tiros a puerta. Las tarjetas se considerarán negativamente.
print("Segun tus prefencias deportivas introduce los siguientes parametros (importancias probabilisticas):")
print("como consejo elije numeros entre 0 y 1")
while True:
    try:
        v1 = float(input("Introduce el valor del porcentaje de posesión: "))
        v2 = float(input("Introduce el valor del porcentaje de pases acertados: "))
        v3 = float(input("Introduce el valor de las asistencias de gol: "))
        v4 = float(input("Introduce el valor de los goles a favor: "))
        v5 = float(input("Introduce el valor de los goles en contra: "))
        v6 = float(input("Introduce el valor de los tiros a puerta: "))
        v7 = float(input("Introduce el valor de los corners: "))
        v8 = float(input("Introduce el valor de las tarjetas amarillas: "))
        v9 = float(input("Introduce el valor de las tarjetas rojas: "))
        break  # Salir del bucle si todas las conversiones son exitosas
    except ValueError:
        print("¡Error! Debes introducir un número decimal (float). Intenta de nuevo.")

weights = {
    'partidos jugados': 0,  # Este valor no influye directamente, más bien normalizaremos otras estadísticas con este
    'porcentaje posesion': v1,
    'porcentaje pases acertados': v2,
    'asistencias de gol': v3,
    'goles a favor': v4,
    'goles en contra': -v5,
    'tiros a puerta': v6,
    'corners': v7,
    'tarjetas amarillas': -v8,
    'tarjetas rojas': -v9
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
while True:
    equipo1 = input("Introduce las siglas del primer equipo : ")
    equipo2 = input("Introduce las siglas del segundo equipo: ")
    
    if equipo1 not in equipos or equipo2 not in equipos:
        print("Al menos uno de los equipos no está en el archivo CSV. Por favor, inténtalo de nuevo.")
    else:
        break

# Ejemplo de predicción entre dos equipos
predict_winner(equipo1, equipo2, data)
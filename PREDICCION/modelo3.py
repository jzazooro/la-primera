# MODELO RANDOM FOREST

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
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

# pide al usuario que introduzca los equipos
while True:
    equipo1 = input("Introduce las siglas del primer equipo : ")
    equipo2 = input("Introduce las siglas del segundo equipo: ")
    
    if equipo1 not in equipos or equipo2 not in equipos:
        print("Al menos uno de los equipos no está en el archivo CSV. Por favor, inténtalo de nuevo.")
    else:
        break

# Corregir los nombres de las columnas para quitar espacios al principio
data.columns = data.columns.str.strip()

# Calcular el promedio de goles por partido para cada equipo
data['goles_promedio_por_partido'] = data['goles a favor'] / data['partidos jugados']

# Preparar las características y la variable objetivo
features = ['porcentaje posesion', 'porcentaje pases acertados', 'tiros a puerta']
X = data[features]
y = data['goles_promedio_por_partido']

# Excluir "BAR" y "MAD" para el conjunto de entrenamiento y usarlos solo para pruebas
train_indices = data[~data['equipo'].isin([equipo1, equipo2])].index
X_train = X.loc[train_indices]
y_train = y[train_indices]

test_indices = data[data['equipo'].isin([equipo1, equipo2])].index
X_test = X.loc[test_indices]
y_test = y[test_indices]

# Crear y entrenar el modelo Random Forest
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Predecir los goles para "BAR" y "MAD"
rf_predicted_goals = rf_model.predict(X_test)
rf_predicted_goals

resultadopredicho =[round(num) for num in rf_predicted_goals]

print(equipo1, resultadopredicho[0], " - ", equipo2, resultadopredicho[1])

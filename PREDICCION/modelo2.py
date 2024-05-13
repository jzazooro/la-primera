import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import csv

# Cargar los datos
file_path = r'DATOS/actualidad.csv'
data = pd.read_csv(file_path)

data.head()

equipos = []

with open(file_path, 'r', newline='') as archivo:
    lector_csv = csv.reader(archivo)
    for fila in lector_csv:
        if fila:  # Verificar si la fila no está vacía
            primer_elemento = fila[0]
            equipos.append(primer_elemento)

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

# Preparar los datos para el modelo
features = ['porcentaje posesion', 'porcentaje pases acertados', 'tiros a puerta']
X = data[features]
y = data['goles_promedio_por_partido']

train_indices = data[~data['equipo'].isin([equipo1, equipo2])].index
X_train = X.loc[train_indices]
y_train = y[train_indices]

test_indices = data[data['equipo'].isin([equipo1, equipo2])].index
X_test = X.loc[test_indices]
y_test = y[test_indices]

# Ajustar el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Predecir los goles promedio por partido
predicted_goals = model.predict(X_test)

# Resultados de la predicción
predicted_goals

resultadopredicho =[round(num) for num in predicted_goals]
print(equipo1, resultadopredicho[0], "-", equipo2, resultadopredicho[1])
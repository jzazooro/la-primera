# MODELO RANDOM FOREST

import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Cargar los datos
data = pd.read_csv('DATOS/actualidad.csv')

# Corregir los nombres de las columnas para quitar espacios al principio
data.columns = data.columns.str.strip()

# Calcular el promedio de goles por partido para cada equipo
data['goles_promedio_por_partido'] = data['goles a favor'] / data['partidos jugados']

# Preparar las características y la variable objetivo
features = ['porcentaje posesion', 'porcentaje pases acertados', 'tiros a puerta']
X = data[features]
y = data['goles_promedio_por_partido']

# Excluir "BAR" y "MAD" para el conjunto de entrenamiento y usarlos solo para pruebas
train_indices = data[~data['equipo'].isin(['BAR', 'MAD'])].index
X_train = X.loc[train_indices]
y_train = y[train_indices]

test_indices = data[data['equipo'].isin(['BAR', 'MAD'])].index
X_test = X.loc[test_indices]
y_test = y[test_indices]

# Crear y entrenar el modelo Random Forest
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Predecir los goles para "BAR" y "MAD"
rf_predicted_goals = rf_model.predict(X_test)
print(rf_predicted_goals)

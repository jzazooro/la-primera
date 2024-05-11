import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Cargar los datos
data = pd.read_csv('DATOS/actualidad.csv')

# Corregir los nombres de las columnas para quitar espacios al principio
data.columns = data.columns.str.strip()

# Calcular el promedio de goles por partido para cada equipo
data['goles_promedio_por_partido'] = data['goles a favor'] / data['partidos jugados']

# Preparar los datos para el modelo
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

# Ajustar el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Predecir los goles promedio por partido para "BAR" y "MAD"
predicted_goals = model.predict(X_test)

# Resultados de la predicción
print(predicted_goals)

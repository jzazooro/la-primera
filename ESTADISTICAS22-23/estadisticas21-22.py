# Primero, necesitamos leer el archivo para entender su estructura y contenido
import pandas as pd

# Cargamos el archivo CSV
data_path = 'DATOS/general21-22.csv'
data = pd.read_csv(data_path)

# Mostramos las primeras filas del dataframe para entender la estructura de los datos
data.head()

# Calculamos la suma total de goles a favor
total_goles = data[' goles a favor'].sum()

# Calculamos la media de goles por partido
media_goles_por_partido = total_goles / 125

# Calculamos la media total de goles en la competición
media_total_goles = media_goles_por_partido * 125

total_goles, media_goles_por_partido, media_total_goles

print("Numero de goles en la competicion: ", media_total_goles)
print("Media de goles por partido en la competicion: ", media_goles_por_partido)

# Calculamos la suma total del valor de equipo
total_valor_equipo = data[' valor de equipo'].sum()

# Calculamos la media del valor de equipo considerando un total de 32 equipos
media_valor_equipo = total_valor_equipo / 32

total_valor_equipo, media_valor_equipo

print("El valor medio de las plantillas de los equipos es: ", media_valor_equipo)

# Calculamos la suma total del coeficiente UEFA
total_coeficiente_uefa = data[' coeficiente uefa'].sum()

# Calculamos la media del coeficiente UEFA considerando un total de 32 equipos
media_coeficiente_uefa = total_coeficiente_uefa / 32

total_coeficiente_uefa, media_coeficiente_uefa

print("El coeficiente UEFA medio de los equipos es: ", media_coeficiente_uefa)


# Eliminar espacios al principio de los nombres de las columnas
data.columns = data.columns.str.strip()

# Calcular la correlación entre 'fase lograda' y 'coeficiente uefa'
correlacion1 = data[['fase lograda', 'coeficiente uefa']].corr()

# Imprimir la matriz de correlación
correlacion1

# Extraer solo el valor de correlación entre 'fase lograda' y 'coeficiente uefa'
valor_correlacion = correlacion1.loc['fase lograda', 'coeficiente uefa']
valor_correlacion

print("El coeficiente de correlacion entre la fase lograda y el coeficiente uefa es de: ", valor_correlacion)
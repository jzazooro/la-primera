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

# Calcular la correlación entre 'fase lograda' y 'valor de equipo'
correlacion2 = data[['fase lograda', 'valor de equipo']].corr()
# Imprimir la matriz de correlación
correlacion2
# Extraer solo el valor de correlación entre 'fase lograda' y 'valor de equipo'
valor_correlacion2 = correlacion2.loc['fase lograda', 'valor de equipo']
valor_correlacion2
print("El coeficiente de correlacion entre la fase lograda y el valor del equipo es de: ", valor_correlacion2)

# Calcular la correlación entre 'fase lograda' y 'diferencia de goles'
correlacion3 = data[['fase lograda', 'diferencia de goles']].corr()
# Imprimir la matriz de correlación
correlacion3
# Extraer solo el valor de correlación entre 'fase lograda' y 'diferencia de goles'
valor_correlacion3 = correlacion3.loc['fase lograda', 'diferencia de goles']
valor_correlacion3
print("El coeficiente de correlacion entre la fase lograda y la diferencia de goles es de: ", valor_correlacion3)

# Calcular la correlación entre 'valor de equipo' y 'diferencia de goles'
correlacion4 = data[['valor de equipo', 'diferencia de goles']].corr()
# Imprimir la matriz de correlación
correlacion4
# Extraer solo el valor de correlación entre 'valor de equipo' y 'diferencia de goles'
valor_correlacion4 = correlacion4.loc['valor de equipo', 'diferencia de goles']
valor_correlacion4
print("El coeficiente de correlacion entre el valor del equipo y la diferencia de goles es de: ", valor_correlacion4)

# Calcular la correlación entre 'valor de equipo' y 'coeficiente uefa'
correlacion5 = data[['valor de equipo', 'coeficiente uefa']].corr()
# Imprimir la matriz de correlación
correlacion5
# Extraer solo el valor de correlación entre 'valor de equipo' y 'coeficiente uefa'
valor_correlacion5 = correlacion5.loc['valor de equipo', 'coeficiente uefa']
valor_correlacion5
print("El coeficiente de correlacion entre el valor del equipo y el coeficiente uefa es de: ", valor_correlacion5)

# Calcular la correlación entre 'diferencia de goles' y 'coeficiente uefa'
correlacion6 = data[['diferencia de goles', 'coeficiente uefa']].corr()
# Imprimir la matriz de correlación
correlacion6
# Extraer solo el valor de correlación entre 'diferencia de goles' y 'coeficiente uefa'
valor_correlacion6 = correlacion6.loc['diferencia de goles', 'coeficiente uefa']
valor_correlacion6
print("El coeficiente de correlacion entre la diferencia de goles y el coeficiente uefa es de: ", valor_correlacion6)
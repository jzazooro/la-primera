# la-primera

El enlace al repositorio de GitHub de este proyecto es el siguiente: [GitHub](https://github.com/jzazooro/la-primera.git)

### OBJETIVO
El objetivo de este proyecto es predecir resultados, identificar comportamientos de apuestas y optimizar estrategias en la edicion 23-24 de la Champions League.

### PROCESO
Hemos recolectado datos de las dos ultimas ediciones de la Champions League ya que son las unicas que no condicional los resultados por la eliminacion de la norma de goles en campo contrario 
valen doble. Al haberlo realizado a mano, no es necesario hacer una limpieza de los datos ya que he seleccionado los que considero que son utiles para hacer este analisis.
He realizado un análisis inicial para identificar tendencias iniciales, patrones y posibles correlaciones entre variable que puedan indicar una distribucion conocida. Posteriormente he ido añadiendo modelos de prediccion en base a las estadisticas de los equipos, estos estan relacionados con un modelo de pesos, regresiones lineales y el uso de la tecnica 
random forest. Los resultados de todos los avances son accesibles ejecutando el main.py y eligiendo cual quieres ver. 

### MODELO 1:  
El primer modelo y mas basico consiste en que el usuario seleccione unos pesos en funcion de la importancia que le da el usuario a cada seccion del juego. Recreando las eliminatorias de la actual edicion de la champions y en funcion de mis prioridades en el juego (30% porcentaje de posesion, 25% porcentaje de pases acertados, 20% asistencias, 30% goles a favor, 
-30% goles en contra, 20% tiros a puerta, 20% corners, -10% amarillas, -15% rojas) el modelo ha predicho que el ganador deberia ser el Manchester City.

### MODELO 2:  
El segundo modelo utiliza una regresion lineal entre los diferentes aspectos del juego de cada equipo y los compara entre si. Recreando las eliminatorias de la actual edicion de la 
champions, el modelo ha predicho que el ganador deberia ser el Real Madrid.

### MODELO 3:  
El ultimo modelo hace uso del random forest para analizar los diferentes aspectos del juego de cada equipo y los compara entre si. Recreando las eliminatorias de la actual edicion de la 
champions, el modelo ha predicho que el ganador deberia ser el PSG.

### CONCLUION
Aunque solo uno de los modelos presenta una posibilidad que se pueda cumplir en la realidad, esto refleja que los datos en el futbol pueden servirde utilidad pero no siempre 
ocurrirá lo que estos dicten a pesar de que la mayoria de partidos si han obtenido un resultado similar a la realidad. Dicho esto muy posiblemente aumentando nuestra base de 
datos podamos obtener mas precision en la prediccion de los eventos deportivos.

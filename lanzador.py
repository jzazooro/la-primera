import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import subprocess

def main():
    visual = input("¿Que datos desea visualizar?"
                   "1. EQUIPOS QUE MAS PUNTOS OBTIENEN EN FASE DE GRUPOS"
                   "2. EQUIPOS QUE MAS GOLES MARCAN EN FASE DE GRUPOS"
                   "3. EQUIPOS QUE MAS GOLES RECIBEN EN FASE DE GRUPOS"
                   "4. EQUIPOS QUE MAS GOLES MARCAN DE LOCAL"
                   "5. EQUIPOS QUE MAS GOLES MARCAN DE VISITANTE"
                   "6. PUNTOS OBTENIDOS DE LOCAL"
                   "7. PUNTOS OBTENIDOS DE VISITANTE"
                   "8. ANALISIS BARCELONA FASE DE GRUPOS"
                   "9. DIAGRAMA DE GOLES MARCADOS EN CASA VS VISITANTE EN FASE DE GRUPOS"
                   "10. PARTIDOS CON GOLES DE AMBOS EQUIPOS VS. PARTIDOS SIN GOLES DE AMBOS EQUIPOS EN TODA LA COMPETICIÓN"
                   "11. MEDIA DE GOLES EN LOS PARTIDOS DE LA COMPETICION Y CORRELACION ENTRE GOLES MARCADOS Y PUNTOS OBTENIDOS"
                   )
    if visual == "1":
        # Ruta al script que quieres ejecutar
        script_path = 'ANALISIS/analisis1.1.py'
        # Ejecutar el script
        subprocess.run(['python', script_path], check=True)
    
    if visual == "2":
        # Ruta al script que quieres ejecutar
        script_path = 'ANALISIS/analisis1.2.py'
        # Ejecutar el script
        subprocess.run(['python', script_path], check=True)

    if visual == "3":
        # Ruta al script que quieres ejecutar
        script_path = 'ANALISIS/analisis1.3.py'
        # Ejecutar el script
        subprocess.run(['python', script_path], check=True)

    if visual == "4":
        # Ruta al script que quieres ejecutar
        script_path = 'ANALISIS/analisis1.4.py'
        # Ejecutar el script
        subprocess.run(['python', script_path], check=True)

    if visual == "5":
        # Ruta al script que quieres ejecutar
        script_path = 'ANALISIS/analisis1.5.py'
        # Ejecutar el script
        subprocess.run(['python', script_path], check=True)

    if visual == "6":
        # Ruta al script que quieres ejecutar
        script_path = 'ANALISIS/analisis1.6.py'
        # Ejecutar el script
        subprocess.run(['python', script_path], check=True)

    if visual == "7":
        # Ruta al script que quieres ejecutar
        script_path = 'ANALISIS/analisis1.7.py'
        # Ejecutar el script
        subprocess.run(['python', script_path], check=True)

    if visual == "8":
        # Ruta al script que quieres ejecutar
        script_path = 'ANALISIS/analisis2.py'
        # Ejecutar el script
        subprocess.run(['python', script_path], check=True)

    if visual == "9":
        # Ruta al script que quieres ejecutar
        script_path = 'ANALISIS/analisis3.py'
        # Ejecutar el script
        subprocess.run(['python', script_path], check=True)

    if visual == "10":
        # Ruta al script que quieres ejecutar
        script_path = 'ANALISIS/analisis4.py'
        # Ejecutar el script
        subprocess.run(['python', script_path], check=True)

    if visual == "11":
        # Ruta al script que quieres ejecutar
        script_path = 'ESTADISTICAS/estadisticas.py'
        # Ejecutar el script
        subprocess.run(['python', script_path], check=True)
    
    if visual != 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10 or 11:
        print("Opción no válida, por favor elige una opción del 1 al 11")

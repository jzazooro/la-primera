import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import subprocess

def main():
    while True:
        visual = input("¿Qué datos desea visualizar?\n"
                       "1. EQUIPOS QUE MÁS PUNTOS OBTIENEN EN FASE DE GRUPOS\n"
                       "2. EQUIPOS QUE MÁS GOLES MARCAN EN FASE DE GRUPOS\n"
                       "3. EQUIPOS QUE MÁS GOLES RECIBEN EN FASE DE GRUPOS\n"
                       "4. EQUIPOS QUE MÁS GOLES MARCAN DE LOCAL\n"
                       "5. EQUIPOS QUE MÁS GOLES MARCAN DE VISITANTE\n"
                       "6. PUNTOS OBTENIDOS DE LOCAL\n"
                       "7. PUNTOS OBTENIDOS DE VISITANTE\n"
                       "8. ANÁLISIS BARCELONA FASE DE GRUPOS\n"
                       "9. DIAGRAMA DE GOLES MARCADOS EN CASA VS VISITANTE EN FASE DE GRUPOS\n"
                       "10. PARTIDOS CON GOLES DE AMBOS EQUIPOS VS. PARTIDOS SIN GOLES DE AMBOS EQUIPOS EN TODA LA COMPETICIÓN\n"
                       "11. MEDIA DE GOLES EN LOS PARTIDOS DE LA COMPETICIÓN Y CORRELACIÓN ENTRE GOLES MARCADOS Y PUNTOS OBTENIDOS\n"
                       "0. Salir\n")
        if visual == "0":
            print("Saliendo del programa.")
            break
        if visual == "1":
            script_path = 'ANALISIS22-23/analisis1.1.py'
        elif visual == "2":
            script_path = 'ANALISIS22-23/analisis1.2.py'
        elif visual == "3":
            script_path = 'ANALISIS22-23/analisis1.3.py'
        elif visual == "4":
            script_path = 'ANALISIS22-23/analisis1.4.py'
        elif visual == "5":
            script_path = 'ANALISIS22-23/analisis1.5.py'
        elif visual == "6":
            script_path = 'ANALISIS22-23/analisis1.6.py'
        elif visual == "7":
            script_path = 'ANALISIS22-23/analisis1.7.py'
        elif visual == "8":
            script_path = 'ANALISIS22-23/analisis2.py'
        elif visual == "9":
            script_path = 'ANALISIS22-23/analisis3.py'
        elif visual == "10":
            script_path = 'ANALISIS22-23/analisis4.py'
        elif visual == "11":
            script_path = 'ESTADISTICAS22-23/estadisticas.py'
        else:
            print("Opción no válida, por favor elige una opción del 0 al 11.")
            continue
        # Ejecutar el script
        try:
            subprocess.run(['python', script_path], check=True)
        except Exception as e:
            print(f"Error al ejecutar el script: {e}")
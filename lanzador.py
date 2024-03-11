import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import subprocess

def main():
    while True:
        visual = input("¿Qué datos desea visualizar?\n"
                       "1. ESTADISTICAS EDICION 21-22\n"
                       "2. ESTADISTICAS EDICION 22-23\n"
                       "3. ANALISIS EDICION 21-22\n"
                       "4. ANALISIS EDICION 22-23\n"
                       "0. Salir\n")
        if visual == "0":
            print("Saliendo del programa.")
            break
        if visual == "1":
            script_path = 'ESTADISTICAS21-22/estadisticas21-22.py'
        elif visual == "2":
            script_path = 'ESTADISTICAS22-23/estadisticas22-23.py'
        elif visual == "3":
            newvisual = input("¿Qué análisis desea visualizar?\n"
                              "1. Puntos Obtenidos por Equipo en la Fase de Grupos\n"
                              "2. Goles Marcados por Equipo en la Fase de Grupos\n"
                              "3. Goles Recibidos por Equipo en la Fase de Grupos\n"
                              "4. Goles Marcados por Equipo de Local en la Fase de Grupos\n"
                              "5. Goles Marcados por Equipo de Visitante en la Fase de Grupos\n"
                              "6. Puntos Obtenidos por Equipo de Local en la Fase de Grupos\n"
                              "7. Puntos Obtenidos por Equipo de Visitante en la Fase de Grupos\n"
                              "8. Rombo city\n"
                              "9. Distribución de Goles Marcados en Casa vs Visitante\n"
                              "10. Partidos con Goles de ambos Equipos vs. Partidos sin Goles de Ambos Equipos\n"
                              )
            if newvisual == "1":
                script_path = 'ANALISIS21-22/analisis1.1.py'
            elif newvisual == "2":
                script_path = 'ANALISIS21-22/analisis1.2.py'
            elif newvisual == "3":
                script_path = 'ANALISIS21-22/analisis1.3.py'
            elif newvisual == "4":
                script_path = 'ANALISIS21-22/analisis1.4.py'
            elif newvisual == "5":
                script_path = 'ANALISIS21-22/analisis1.5.py'
            elif newvisual == "6":
                script_path = 'ANALISIS21-22/analisis1.6.py'
            elif newvisual == "7":
                script_path = 'ANALISIS21-22/analisis1.7.py'
            elif newvisual == "8":
                script_path = 'ANALISIS21-22/analisis1.8.py'
            elif newvisual == "9":
                script_path = 'ANALISIS21-22/analisis1.9.py'
            elif newvisual == "10":
                script_path = 'ANALISIS21-22/analisis1.10.py'
            else:
                print("Opción no válida, por favor elige una opción del 0 al 10.")
                continue
        elif visual == "4":
            newvisual = input("¿Qué análisis desea visualizar?\n"
                              "1. Puntos Obtenidos por Equipo en la Fase de Grupos\n"
                              "2. Goles Marcados por Equipo en la Fase de Grupos\n"
                              "3. Goles Recibidos por Equipo en la Fase de Grupos\n"
                              "4. Goles Marcados por Equipo de Local en la Fase de Grupos\n"
                              "5. Goles Marcados por Equipo de Visitante en la Fase de Grupos\n"
                              "6. Puntos Obtenidos por Equipo de Local en la Fase de Grupos\n"
                              "7. Puntos Obtenidos por Equipo de Visitante en la Fase de Grupos\n"
                              "8. Rombo barsa\n"
                              "9. Distribución de Goles Marcados en Casa vs Visitante\n"
                              "10. Partidos con Goles de ambos Equipos vs. Partidos sin Goles de Ambos Equipos\n"
                              )
            if newvisual == "1":
                script_path = 'ANALISIS22-23/analisis2.1.py'
            elif newvisual == "2":
                script_path = 'ANALISIS22-23/analisis2.2.py'
            elif newvisual == "3":
                script_path = 'ANALISIS22-23/analisis2.3.py'
            elif newvisual == "4":
                script_path = 'ANALISIS22-23/analisis2.4.py'
            elif newvisual == "5":
                script_path = 'ANALISIS22-23/analisis2.5.py'
            elif newvisual == "6":
                script_path = 'ANALISIS22-23/analisis2.6.py'
            elif newvisual == "7":
                script_path = 'ANALISIS22-23/analisis2.7.py'
            elif newvisual == "8":
                script_path = 'ANALISIS22-23/analisis2.8.py'
            elif newvisual == "9":
                script_path = 'ANALISIS22-23/analisis2.9.py'
            elif newvisual == "10":
                script_path = 'ANALISIS22-23/analisis2.10.py'
            else:
                print("Opción no válida, por favor elige una opción del 0 al 10.")
                continue
        # Ejecutar el script
        try:
            subprocess.run(['python', script_path], check=True)
        except Exception as e:
            print(f"Error al ejecutar el script: {e}")
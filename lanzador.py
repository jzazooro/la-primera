import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import subprocess

def main():
    while True:
        visual = input("¿Qué datos desea visualizar?\n"
                       "1. ESTADISTICAS EDICION 21-22\n"
                       "2. ESTADISTICAS EDICION 22-23\n"
                       "3. \n"
                       "4. \n"
                       "5. \n"
                       "6. \n"
                       "7. \n"
                       "8. \n"
                       "9. \n"
                       "10. \n"
                       "11. \n"
                       "0. Salir\n")
        if visual == "0":
            print("Saliendo del programa.")
            break
        if visual == "1":
            script_path = 'ESTADISTICAS21-22/estadisticas21-22.py'
        elif visual == "2":
            script_path = 'ESTADISTICAS22-23/estadisticas22-23.py'
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
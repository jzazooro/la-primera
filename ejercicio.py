# Importando la biblioteca necesaria para trabajar con archivos binarios
import subprocess

# Función para extraer las cadenas de un archivo binario
def extract_strings(file_path):
    # Comando para extraer cadenas de un archivo binario
    try:
        result = subprocess.run(['strings', file_path], capture_output=True, text=True)
        return result.stdout.splitlines()  # Devolvemos las líneas de salida como una lista de cadenas
    except Exception as e:
        return str(e)

# Ruta al archivo binario subido
file_path = 'flag'

# Extraer cadenas del archivo binario
extracted_strings = extract_strings(file_path)
extracted_strings[:10]  # Mostrar solo las primeras 10 cadenas para revisión inicial


#parte2 
# Mostrar más cadenas extraídas para intentar identificar alguna relevante
extracted_strings


#parte3
# Función para descifrar una cadena con cifrado César sobre el rango ASCII completo
def caesar_cipher(text, shift):
    return ''.join(chr((ord(char) - shift) % 256) for char in text)

# Cadena sospechosa que podría ser una cadena mágica cifrada
encrypted_string = "v7z7vw5rkcrsciwchmjmgmp"

# Probar todas las posibles desviaciones para el cifrado César (1 a 255)
decrypted_variants = [(shift, caesar_cipher(encrypted_string, shift)) for shift in range(1, 256)]

# Mostrar algunos de los resultados para revisar manualmente
decrypted_variants[:10]  # Mostrando solo las primeras 10 variantes para evitar una salida demasiado larga

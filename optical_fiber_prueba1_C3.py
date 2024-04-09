import json
import time

# Ruta del archivo JSON en la máquina virtual
ruta_archivo = "/home/devasc/labs/devnet-src/parsing/myfile.json"

# Intentar abrir el archivo JSON
try:
    with open(ruta_archivo) as archivo:
        data = json.load(archivo)
    print("Archivo JSON cargado correctamente.")

    # Obtener el access_token y el expires_in
    access_token = data.get("access_token")
    expires_in_segundos = data.get("expires_in")

    # Calcular cuánto tiempo queda antes de que caduque el token
    tiempo_actual = int(time.time())
    tiempo_caducidad = tiempo_actual + expires_in_segundos
    tiempo_restante_segundos = tiempo_caducidad - tiempo_actual
    tiempo_restante_minutos = tiempo_restante_segundos // 60

    # Imprimir el valor del access_token y el tiempo restante antes de la caducidad
    print("Valor del access_token:", access_token)
    print("Tiempo restante antes de la caducidad del token:", tiempo_restante_minutos, "minutos")

except FileNotFoundError:
    print("El archivo JSON no se encontró en la ruta especificada.")
except json.JSONDecodeError:
    print("Error al decodificar el archivo JSON.")

import json

# Ruta del archivo JSON en la máquina virtual
ruta_archivo = "/home/devasc/labs/devnet-src/parsing/myfile.json"

# Intentar abrir el archivo JSON
try:
    with open(ruta_archivo) as archivo:
        json_file = json.load(archivo)
    print("Archivo JSON cargado correctamente.")
except FileNotFoundError:
    print("El archivo JSON no se encontró en la ruta  especificada.")
except json.JSONDecodeError:
    print("Error al decodificar el archivo JSON.")

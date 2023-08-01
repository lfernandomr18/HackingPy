import json
import urllib.request
from os import path

def main():
    # Obtener la ruta completa del archivo JSON
    #forma portable de poder encontrar el path(directorio)
    file_path = path.join(path.dirname(__file__), 'jsonUsers.json')

    # Leer el archivo JSON y cargar el contenido en 'data'
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    for user in data:
        user_slug = user['slug']
        print(user_slug)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Saliendo...")


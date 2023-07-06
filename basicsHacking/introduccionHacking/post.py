import requests
import argparse
from os import path


parser= argparse.ArgumentParser(description="Post")
parser.add_argument('-f','--file',help="Indica el archivo a subir")
parser= parser.parse_args()

def main():
    if parser.file:
        if path.exists(parser.file):
            archivo = open(parser.file,'rb')
            headers={'User-Agent':'Firefox'}
            url=input("Ingresa la URL: ")
            textoParam=str(input("Ingresa el parametro: "))
            peticion = requests.post(url, files={textoParam:archivo}, headers=headers)
            if parser.file in peticion.text:
                print("Archivo Subido con Exito")
            else:
                print(peticion)
                print("Fallo la subido del archivo")
        else:
            print("No existe el archivo")
    else:
        print("Necesito un archivo para subir")



if __name__ =='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Saliendo...")
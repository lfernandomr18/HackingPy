import requests
import argparse

parser= argparse.ArgumentParser(description="Detector de cabeceras")
parser.add_argument('-t','--target',help="objetivo")
parser= parser.parse_args()


def main():
    if parser.target:
        try:
            url=requests.get(url=parser.target)
            cabeceras=dict(url.headers)
            for c in cabeceras:
                print("\n"+c+" : "+cabeceras[c])
        except:
            print("No me pude conectar")
    else:
        print("No hay objetivo")

if __name__ =='__main__':
    main()
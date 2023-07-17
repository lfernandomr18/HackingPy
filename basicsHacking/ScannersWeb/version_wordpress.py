import requests
from bs4 import BeautifulSoup


def main():
    url="https://fivethirtyeight.com/"
    cabecera={'User-Agent': 'Firefox'}
    print(cabecera)
    peticion=requests.get(url=url,headers=cabecera)
    p=BeautifulSoup(peticion.text,'html5lib')
    for link in p.find_all('meta'):
        if link.get('name')=='generator':
            print(link.get('content'))
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Saliendo...")
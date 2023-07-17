import mechanize
import argparse
import time
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("-b", "--buscar", help="Opción a buscar")
parser = parser.parse_args()

# Definir el tiempo de espera entre las solicitudes (en segundos)
DELAY_TIME = 20

def main():
    if parser.buscar:
        bus = mechanize.Browser()
        bus.set_handle_robots(False)
        bus.set_handle_equiv(False)
        bus.set_debug_responses(False)
        bus.clear_history()
        bus.addheaders = [('User-Agent', 'Firefox')]
        bus.open("https://duckduckgo.com/")
        for n in bus.forms():
            print(n)
        bus.select_form(nr=0)
        bus['q'] = parser.buscar
        try:
            bus.submit()
            response_content = bus.response().read()
            p=BeautifulSoup(response_content,'html5lib')
            lasturl=''
            for link in p.find_all('a'):
                if link.get('href') == lasturl:
                    pass
                else:
                    
                    print('esto contiene Texto del Link: ',link.string)                   
                    print('imprimiento el href: ',link.get('href'))
                    print('******************************')
                    lasturl=link.get('href')            
        except mechanize.HTTPError as e:
            if e.code == 429:
                print("Demasiadas solicitudes. Esperando {} segundos...".format(DELAY_TIME))
                print(e)
                time.sleep(DELAY_TIME)
                main()  # Hacer una llamada recursiva para reintentar la solicitud
            else:
                print("Se produjo un error HTTP:", e.code)
    else:
        print("Palabra a buscar")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Saliendo...")

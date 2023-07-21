import requests
from bs4 import BeautifulSoup

def get_response(url):
    response = requests.get(url)
    html = response.text
    return html
def parseHtmlFromUrl(html):
    return BeautifulSoup(html, 'html.parser')  
def printTitle(soup):
    title = soup.find('title')
    print(title.text)
    print('*************************')
def printAllh1(soup):
    list_h1 = soup.find_all('h1')
    number=0
    print('PRINTING ALL H1: ')
    for h1 in list_h1:
        print(number,' -- ',h1)
        number =number+1
    print('*************************')
def getH1(soup, max_h1):
    if not isinstance(max_h1, int):
        print("El segundo parámetro debe ser un número entero.")
        return
    list_h1 = soup.find_all('h1')
    print('PRINTING H1 AT POSITION : {}'.format(max_h1))
    print(list_h1[max_h1].text.strip())
    print('*************************')
def getSoup(url):
    html = get_response(url)
    return parseHtmlFromUrl(html)
def getClinicName(clinicId):
    url=f'https://{clinicId}.portal.athenahealth.com/'
    soup=getSoup(url=url)
    return  soup.find_all('h1')[-1].text.strip()

def main():
    print(getClinicName(clinicId=12695))
    print(getClinicName(clinicId=12696))
    print(getClinicName(clinicId=12697))
    
    

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Saliendo...")

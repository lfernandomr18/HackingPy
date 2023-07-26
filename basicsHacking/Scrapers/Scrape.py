import requests
from bs4 import BeautifulSoup
import pandas as pd
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
def generateCsv(start,end):
    master_list=[]
    try:
        for clinic_id in range(start,end):
           data_dict={}
           data_dict['clinic_id']=clinic_id
           data_dict['clinic_name']=getClinicName(clinicId=clinic_id)
           print(data_dict['clinic_name'])
           if data_dict['clinic_name'] !='Payment Confirmation' and data_dict['clinic_name'] !="Sorry, we can't find that practice. Make sure you typed the right address.":
            master_list.append(data_dict)
    except Exception as e:
        print("An exception occurred:", e)
    finally:
        df=pd.DataFrame(master_list)
        df.to_csv('clinic_data.csv',index=False)
        print('*******************************')
        print('TOMA AWITA CTMR TE QUIERO MUCHO')


def main():
    start=12690
    end=12695
    generateCsv(start=start,end=end)
    

    
    

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Saliendo...")

import json
import requests
from os import path





def main():
    #una manera de escapar de un error 403 es usar Headers
    #https://scrapeops.io/web-scraping-playbook/403-forbidden-error-web-scraping/#:~:text=Optimize%20Request%20Headers%E2%80%8B,to%20optimize%20the%20request%20headers.
    web=input("introduce la web wordpress: ")
    HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
    r=requests.get(web,headers=HEADERS)
    data=json.loads(r.text)
    
    # aca se imprime los usuarios wordpress del lugar    
    for user in data:
        user_slug = user['slug']
        print(user_slug)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Saliendo...")

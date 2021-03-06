import requests
import threading
from termcolor import colored
import time
import queue

start = time.time()

xbox_gtin = "0889842640809"
ps5_gtin = "0711719395201"

url="https://www.carrefour.fr/api/v1/offer_locator?gtin=" + xbox_gtin + "&postalCode="

headers = {
  'authority': 'www.carrefour.fr',
  'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
  'accept': 'application/json, text/plain, */*',
  'x-dtpc': '4$374935134_730h16vRHFEUHWRLFEMUMCJOCATHLWHOWFHUSPU-0e0',
  'x-requested-with': 'XMLHttpRequest',
  'sec-ch-ua-mobile': '?0',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://www.carrefour.fr/p/console-xbox-series-x-1to-microsoft-0889842640809',
  'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
}

stores_with_stock = []
threads = []

def lookForStockIn(stores_with_stock, postal_code):
    response = requests.request("GET", url + postal_code, headers=headers)
    if "errors" not in response.json():
        for store in response.json()["data"]["attributes"]["stores"]:
            if(store["isProductAvailable"] == True):
                stores_with_stock.append({'store':store["store"]["name"], 'code': postal_code})

print(colored('Recherche de stocks en cours...', 'cyan'))

for i in range(1, 96):
    if i < 10 :
        postal_code_start = "0" + str(i)
    else:
        postal_code_start = str(i)
    for j in range(1,10):
        postal_code = postal_code_start + str(j) + "00"
        thread = threading.Thread(target=lookForStockIn, args=(stores_with_stock ,postal_code,))
        thread.start()
        threads.append(thread)
        time.sleep(0.05)

for thread in threads:
    thread.join()

print(colored('\n\nRésultats :', 'green'))

print('Durée de la recherche : {0:0.1f} secondes'.format(time.time() - start))

if(len(stores_with_stock) == 0):
    print(colored('Aucune console disponible :(', 'red'))
else:
    print(colored('Du stock a été trouvé dans ' + str(len(stores_with_stock)) + ' magasins. Les voici : \n', 'green'))

for store in stores_with_stock:
    print('- ' + store['store'] + ' dans le ' + store['code'])
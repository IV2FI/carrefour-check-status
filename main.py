import requests
from termcolor import colored
import time

start = time.time()

xbox_gtin = "0889842640809"

url="https://www.carrefour.fr/api/v1/offer_locator?gtin=" + xbox_gtin + "&postalCode="

headers = {
  'x-requested-with': 'XMLHttpRequest'
}

stores_with_stock = []

for i in range(1, 96):
    if i < 10 :
        postal_code_start = "0" + str(i)
    else:
        postal_code_start = str(i)
    print(colored('Recherche de stocks dans le ' + postal_code_start + '...', 'cyan'))
    for j in range(1,10):
        postal_code = postal_code_start + str(j) + "00"
        response = requests.request("GET", url + postal_code, headers=headers)
        if "errors" not in response.json():
            for store in response.json()["data"]["attributes"]["stores"]:
                if(store["isProductAvailable"] == True): 
                    print(colored('Trouvé à ' + store["store"]["name"] + ' dans le ' + postal_code_start, 'green'))
                    stores_with_stock.append({'store':store["store"]["name"], 'code': postal_code})

print(colored('\n\nRésultats :', 'green'))

print('Durée de la recherche : {0:0.1f} secondes'.format(time.time() - start))

if(len(stores_with_stock) == 0):
    print(colored('Aucune console disponible :(', 'red'))
else:
    print(colored('Du stock a été trouvé ! Voici le(s) magasin(s) avec du stock : \n', 'green'))

for store in stores_with_stock:
    print('- ' + store['store'] + ' dans le ' + store['code'])





"""
Author: Youssef Abbas 
GitHuv : https://github.com/jooabbas99
Shopify Products scrapping 

HOW TO USE : 
python3 shopify_scraper.py [DOMAIN]
"""
import sys
import requests
import json
if __name__ == '__main__':
    domian = sys.argv[1]
    products = []
    while(True):
        url = f'https://{domian}/products.json?limit=250&page={i}'
        data = requests.get(url)
        if len(data.json()['products']) == 0:
            break
        json_data = data.json()

        for j in json_data['products']:
            products.append(j)
    print('items found : ' + str(len(products)))
    with open(f'{domian}_products.json', 'w') as f:
        json.dump(products, f)
            

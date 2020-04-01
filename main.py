from builtins import print

import requests
from bs4 import BeautifulSoup


def print_title(string):
    print('TITULO: {}'.format(string))


def print_price_efectivo(string):
    print('PRECIO Efectivo: {}'.format(string))


def print_price_tarjeta(string):
    print('PRECIO Tarjeta: {}'.format(string))


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  'Chrome/80.0.3987.149 Safari/537.36'
}

# Caso SPDIGITAL

URL = 'https://www.spdigital.cl/products/view/68271'

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id='_name')
title_value = title.get_text().strip()

div_price_efectivo = soup.find_all('div', {
    'class': 'product-view-cash-price-div'
})

price_efectivo = None

for element in div_price_efectivo:
    price_efectivo = element.find('span', {
        'class': 'product-view-cash-price-value text-webstore'
    })


div_price_tarjeta = soup.find_all('div', {
    'class': 'product-view-other-method-price-div'
})

price_tarjeta = None

for element in div_price_tarjeta:
    price_tarjeta = element.find('span', {
        'class': 'product-view-cash-price-value text-webstore'
    })

# Muestra información en pantalla
print_title(title_value)
if price_efectivo is not None:
    price_efectivo_value = price_efectivo.get_text().strip()
    print_price_efectivo(price_efectivo_value)

if price_tarjeta is not None:
    price_tarjeta_value = price_tarjeta.get_text().strip()
    print_price_tarjeta(price_tarjeta_value)

print('--------------')

# Caso Sistemax

URL = 'https://www.sistemax.cl/index.php?route=product/product&product_id=1974'

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find_all('h1')
title_value = title[0].get_text().strip()

price_tarjeta = soup.find(id='tar')
price_tarjeta_value = price_tarjeta.get_text().strip()

price_efectivo = soup.find(id='pe')
price_efectivo_value = price_efectivo.get_text().strip()

# Muestra información en pantalla
print_title(title_value)
print_price_tarjeta(price_tarjeta_value)
print_price_efectivo(price_efectivo_value)

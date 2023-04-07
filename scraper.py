import requests
from bs4 import BeautifulSoup
import array
productlist = ["ryzen 7600x", "ryzen 7700x", "ryzen 7900x"]
for product in productlist:
    search_query = product
    #search_query = input("enter input:\n")
    search_query = search_query.replace(' ', '+') 
    url = 'https://www.bestprice.gr/search?q='+search_query
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    price_elem = soup.find('div', {'class': 'p__price--current'})
    name_elem = soup.find('h3', {'class': 'p__title p__title--lines p__title--lines-2'})
    if price_elem:
        price = price_elem.get_text().strip()
        name = name_elem.get_text().strip()
        print(name)
        print(price)
    else:
        print('Not found')

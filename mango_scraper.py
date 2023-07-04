import requests
from bs4 import BeautifulSoup

url = 'https://shop.mango.com/us/women'

res = requests.get(url)
html_page = res.content

soup = BeautifulSoup(html_page, 'html.parser')

strings_list = []
for string in soup.stripped_strings:
    strings_list.append(repr(string))

sale_candidates = set()
for string in strings_list:
    if '%' in string:
        sale_candidates.add(string)

if len(sale_candidates) == 0:
    print("Could not find sale")
    

print(sale_candidates)

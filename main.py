import requests
from bs4 import BeautifulSoup

ebay_url = "https://www.ebay.com/itm/234734868502?hash=item36a749d816:g:7n4AAOSw5oRjSdTj&amdata=enc%3AAQAHAAAAoDr0gUlPFRQrdBqYdve%2BTDwXs9AXsQW6P15TIwnLKfSb7B7ZyH12KCteHWQjsDaXiAqAxHXrtlhYU6bxKwREy6qaMSvwo1w3exdE1hTXc%2F7XxlGdRhf6lm0k%2BlibMNbVSfPK0VSrs73PyL4d1in4Uwrmt1wkcsx4a9nOOVrutwcd4FfcT00yUhWky0mnPF1o5eXP7PA6Wq%2Fa9lIZDdCI2rw%3D%7Ctkp%3ABk9SR76E0On-YA"
response = requests.get(ebay_url)
soup = BeautifulSoup(response.text, "html.parser")
title = soup.findAll('span', class_="ux-textspans ux-textspans--BOLD",recursive=True)
price = soup.findAll('span', class_="notranslate",recursive=True)
item_descr_url = 'https://vi.vipr.ebaydesc.com/ws/eBayISAPI.dll?item={item_id}'
item_id = ebay_url.split('?')[0].split('/')[-1]
soupdesc = BeautifulSoup(requests.get(item_descr_url.format(item_id=item_id)).content, 'html.parser')
list1=[]
list1.append("Title : ")
list1.append(title[1].text)
list1.append("Listing URL : ")
list1.append(ebay_url)
list1.append("Price : ")
list1.append(price[0].text)
list1.append("Item Detail : ")
list1.append(soupdesc.get_text(strip=True, separator='\n').split("\n")[2])
with open('c:/meow/ferrari.txt', 'w') as f:
    for line in list1:
        f.write(line)
        f.write('\n')
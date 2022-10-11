from cgitb import html, text
from csv import excel
from logging import exception
import requests
from itertools import product
from statistics import mode
from turtle import title
from urllib import response
from bs4 import BeautifulSoup
import requests, openpyxl
import json
# //create excel file

excel = openpyxl.Workbook()

# print(excel.sheetnames)

# /micheline
# url = "https://www.tyroola.com.au/tyre/michelin/pcr/pilot-sport-4/?buy_3_for_4=0&instant_cash=0&clearance=0&rft=0"
# briodgestone
# url = 'https://www.tyroola.com.au/tyre/bridgestone/turanza-t005/'
# Kumho Road
# url = "https://www.tyroola.com.au/tyre/kumho/road-venture-mt51/"
#dunlop
# url= "https://www.tyroola.com.au/tyre/dunlop/sp-sport-lm705/?o=24"
# pirelli
# url = "https://www.tyroola.com.au/v1/tyre/pirelli/?o=48"
# bfGoodRich




# url = "https://www.tyroola.com.au/tyre/dunlop/225-60-r17/"

url = "https://www.tyroola.com.au/tyre/hankook/dynapro-atm-rf10/"


response = requests.get(url)
print(response.status_code)

htmlcontent = response.content
soup = BeautifulSoup(htmlcontent, 'html.parser')
sheet = excel.active
sheet.title = "Micheline Tyres"
print(excel.sheetnames)
sheet.append(['Brand Name', 'Model Name', 'Size', 'Image Link', 'Stock', 'Price'])

brandfullname = []
models = []
sizes = []
prices = []
images = []
stocks = []

# value = json.loads(soup.find_all('script', type='application/ld+json').text)
# print(value)

# //get all url

for ur in soup.find_all('a', attrs={'class': 'link-list-slider__link'}):
    allurl =  ur.get('href')

for data in soup.find_all('div', attrs={'class': 'product-tile'}):
    # print(data)
    brandname = data.find('img')
    fullname = brandname.get('alt')
    image = data.find('img', attrs={'class': 'product-tile__image'})
    imagelink = (image.get('data-original'))
    # print(image.get('data-original'))
    model = data.find('div', attrs={'class': 'product-tile__model'})
    mod = model.string
    # print(model.string)
    size = data.find('div', attrs={'class': 'product-tile__size'})
    si = size.string
    # print(size.string)
    # ea = data.find('span', attrs={'class': 'product-tile__price-current-ea'})
    # value = data.find('div', class_="product-tile__price-current").span.text 
    value = data.find('span', class_="product-tile__price-current-value").get_text()
    # print(value)

    try:
        findStock = data.find('span', class_="product-tile__stock-notification-label").get_text()
        # print(findStock)
    except:
        findStock = "None"
    # value = data.find('div', class_="product-tile__price-current").span(0).text
    # print(fullname, mod, si,value)
    sheet.append([fullname, mod, si, imagelink, findStock, value])
    

# for stock in soup.find_all('div', class_="product-tile__product-notification"):
 




# name = brandfullname.append(brandname.get('alt'))
# model = models.append(model.string)
# image = images.append(image.get('data-original'))
# price = prices.append(value)
# size = sizes.append(size.string)

excel.save('matrax1.xlsx')






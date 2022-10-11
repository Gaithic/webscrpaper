from cgitb import html, text
from csv import excel
from logging import exception
import requests
from itertools import product
from statistics import mode
from turtle import title
from urllib import request, response
from bs4 import BeautifulSoup
import requests, openpyxl
import json
# //create excel file

excel = openpyxl.Workbook()


url = "https://www.tyroola.com.au/tyre/federal/"


response = requests.get(url)
# print(response.status_code)

htmlcontent = response.content
soup = BeautifulSoup(htmlcontent, 'html.parser')

allurl = []
excelname = 'excelsheet'

sheet = excel.active
sheet.title = "Micheline Tyres"
# print(excel.sheetnames)
sheet.append(['Brand Name', 'Model Name', 'Size', 'Image Link', 'Stock', 'Price'])

for ur in soup.find_all('a', attrs={'class': 'link-list-slider__link'}):
    # allurl.append(ur.get('href'))
    url = 'https://www.tyroola.com.au/'+(ur.get('href'))
    response = requests.get(url)
    # print(response.status_code)
    htmlcontent = response.content
    soup = BeautifulSoup(htmlcontent, 'html.parser')

    sheet = excel.active
    sheet.title = "Micheline Tyres"
    print(excel.sheetnames)
    # sheet.append(['Brand Name', 'Model Name', 'Size', 'Image Link', 'Stock', 'Price'])

    brandfullname = []
    models = []
    sizes = []
    prices = []
    images = []
    stocks = []
    count = 0
    for data in soup.find_all('div', attrs={'class': 'product-tile'}):
        # print(data)
        brandname = data.find('img')
        fullname = brandname.get('alt')
        print(fullname)
        image = data.find('img', attrs={'class': 'product-tile__image'})
        imagelink = (image.get('data-original'))
        
        model = data.find('div', attrs={'class': 'product-tile__model'})
        mod = model.string
        
        size = data.find('div', attrs={'class': 'product-tile__size'})
        si = size.string
    
        value = data.find('span', class_="product-tile__price-current-value").get_text()
        try:
            findStock = data.find('span', class_="product-tile__stock-notification-label").get_text()
        except:
            findStock = "None"
        sheet.append([fullname, mod, si, imagelink, findStock, value])
        count = +1
        excel.save('fedral'+'sheet.xlsx')

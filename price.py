from cgitb import html, text
from csv import excel
from dataclasses import dataclass
from logging import exception
import requests
from itertools import product
from statistics import mode
from turtle import title
from urllib import request, response
from bs4 import BeautifulSoup
import requests, openpyxl
import json
import ast
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
    script = soup.find_all('script')[3].text.strip()[19:-366]
    data = json.loads(json.dumps(script).strip())
    
    parsed_json = ast.literal_eval(data)
    print(parsed_json)

    # for val in parsed_json:
    #     transactionId = parsed_json[val]['transaction_id']
    #     listName = parsed_json[val]['list_name']
    #     listPosition = parsed_json[val]['list_position']
    #     name = parsed_json[val]['name']
    #     brand = parsed_json[val]['brand']
    #     category = parsed_json[val]['category']
    #     variant = parsed_json[val]['variant']
    #     price =parsed_json[val]['price']
    #     sheet.append([transactionId, listName, listPosition, name, brand, category, variant, price])
    #     excel.save('matrax.xlsx')






# r = requests.get(url)
# soup = BeautifulSoup(r.content, 'html.parser')
# script = soup.find_all('script')[3].text.strip()[19:-366]
# print(script)
# # f = open('url')
# data = json.loads(json.dumps(script))
# # data = json.loads(script)
# # print(data)
# parsed_json = ast.literal_eval(data)
# # print(parsed_json['TY599103D214'])
# # //make array to store date

# imagelin = []
# tran = []
# lina = []
# for data in soup.find_all('div', attrs={'class': 'product-tile'}):
#     image = data.find('img', attrs={'class': 'product-tile__image'})
#     imagelink = (image.get('data-original'))
#     imagelin.append(imagelink)

# for val in parsed_json:
#     transactionId = parsed_json[val]['transaction_id']
#     tran.append(transactionId)
#     listName = parsed_json[val]['list_name']
#     lina.append(listName)
#     listPosition = parsed_json[val]['list_position']
#     name = parsed_json[val]['name']
#     brand = parsed_json[val]['brand']
#     category = parsed_json[val]['category']
#     variant = parsed_json[val]['variant']
#     price =parsed_json[val]['price']
#     sheet.append([transactionId, listName, listPosition, name, brand, category, variant, price])
#     excel.save('matrax.xlsx')
from gettext import translation
from hashlib import new
from tkinter.font import names
from urllib import response
import requests
import json
from bs4 import BeautifulSoup
import requests, openpyxl
import ast


excel = openpyxl.Workbook()

print(excel.sheetnames)


url = "https://www.tyroola.com.au/tyre/michelin/pcr/pilot-sport-4/?buy_3_for_4=0&instant_cash=0&clearance=0&rft=0"


sheet = excel.active
sheet.title = "Micheline Tyres"
print(excel.sheetnames)
sheet.append(['transaction_id', 'list_name', 'list_position', 'name', 'brand', 'category', 'variant', 'price', 'image-Link'])


r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
script = soup.find_all('script')[3].text.strip()[19:-366]
# f = open('url')
data = json.loads(json.dumps(script))
# data = json.loads(script)
# print(data)
parsed_json = ast.literal_eval(data)
# print(parsed_json['TY599103D214'])
# //make array to store date

imagelin = []
tran = []
lina = []
for data in soup.find_all('div', attrs={'class': 'product-tile'}):
    image = data.find('img', attrs={'class': 'product-tile__image'})
    imagelink = (image.get('data-original'))
    imagelin.append(imagelink)

for val in parsed_json:
    transactionId = parsed_json[val]['transaction_id']
    tran.append(transactionId)
    listName = parsed_json[val]['list_name']
    lina.append(listName)
    listPosition = parsed_json[val]['list_position']
    name = parsed_json[val]['name']
    brand = parsed_json[val]['brand']
    category = parsed_json[val]['category']
    variant = parsed_json[val]['variant']
    price =parsed_json[val]['price']
    sheet.append([transactionId, listName, listPosition, name, brand, category, variant, price])
    


# print(imagelin, tran, lina)

excel.save('micheline tierss.xlsx')


# print(parsed_json['TY599103D214']['price'])

# print(main)
# print(main)['price']
# new_parsed_json = ast.literal_eval(main)
# print(new_parsed_json)

# for i in range(len(main)):
#     print(main[i]['price'])


# print(data)['TY599103D214']
# above code i right code

# jsonData = data["TY599103D214"]['price']

# print(data)
# for i in data['TY599103D214']:
#     print(i)
# print(data)
# print(data)['TY599103D214']
# for val in  data:
#     print(val[0:100])
# sheet.append([data])
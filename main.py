import requests
import xml.etree.ElementTree as ET
from urllib.request import urlopen

url = "http://www.tcmb.gov.tr/kurlar/today.xml"
resp = requests.get(url=url)
print(resp.text)
tree = ET.parse(urlopen(url))
root = tree.getroot()


liste= []
liste.append(root.findall('Currency'))


for i in liste[0]:
    currencyCode = i.get('Kod')
    banknoteBuying = i.find("BanknoteBuying").text
    banknoteSelling = i.find("BanknoteSelling").text
    name = i.find("Isim").text

    if currencyCode == 'USD':
        result = float(banknoteSelling) - float(banknoteBuying)
        print("Para Birimi Adı: ", name)
        print("USD", banknoteSelling)
        print("USD",banknoteBuying)
        print("Banka alış-satış arasındaki kur farkı: ",str(result))

    if currencyCode == 'EUR':
        print("Para Birimi Adı: ", name)
        print("EUR", banknoteSelling)
        print("EUR", banknoteBuying)
        result = float(banknoteSelling) - float(banknoteBuying)
        print("Banka alış-satış arasındaki kur farkı: ", str(result))


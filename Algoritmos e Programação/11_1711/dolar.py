import requests
from bs4 import BeautifulSoup
import re
import math
from tkinter import *

url = ('https://www.google.com/search?q=dolar&oq=dolar&aqs=chrome.0.69i59l3j0i131i433i512j69i60j69i61j69i60l2.552j1j7&sourceid=chrome&ie=UTF-8')

headers = {'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
dol = float(soup.find('span', class_='DFlfde SwHCTb').get_text().replace(",", "."))

moeda = str(input("Qual sua moeda atual: "))
valor = float(input("Qual o valor: "))

if moeda == "dolar":
    conversao = valor*dol
    print("")
    print("---------------------------------------")
    print("Voçê tem: U$",valor)
    print(f"A quantidade em reais é: R${conversao:.2f}")
    print("Cotação do dolar atual: R$",dol)
    print("---------------------------------------")
    print("")
elif moeda == "real":
    conversao = valor/dol
    print("")
    print("---------------------------------------")
    print("Você tem :R$", valor)
    print(f"A quantidade em dolar é: R${conversao:.2f}")
    print("Cotação atual do dolar: R$",dol)
    print("---------------------------------------")
    print("")
else:
    print("Errrrrou")
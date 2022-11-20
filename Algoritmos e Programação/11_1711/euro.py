import requests
from bs4 import BeautifulSoup
import re
import math
from tkinter import *

url = ('https://www.google.com/search?q=euro&oq=euro&aqs=chrome..69i57j0i131i433i512j0i433i512j46i433i512j0i433i512j69i60l3.638j1j7&sourceid=chrome&ie=UTF-8')

headers = {'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
dol = float(soup.find('span', class_='DFlfde SwHCTb').get_text().replace(",", "."))

moeda = str(input("Qual sua moeda atual: "))
valor = float(input("Qual o valor: "))

if moeda == "euro":
    conversao = valor*dol
    print("")
    print("---------------------------------------")
    print("Voçê tem: UR$",valor)
    print(f"A quantidade em reais é: R${conversao:.2f}")
    print("Cotação do euro atual: R$",dol)
    print("---------------------------------------")
    print("")
elif moeda == "real":
    conversao = valor/dol
    print("")
    print("---------------------------------------")
    print("Você tem :R$", valor)
    print(f"A quantidade em euro é: R${conversao:.2f}")
    print("Cotação atual do euro: R$",dol)
    print("---------------------------------------")
    print("")
else:
    print("Errrrrou")
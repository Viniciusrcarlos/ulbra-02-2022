import requests
from bs4 import BeautifulSoup
import re
import math
from tkinter import *
#Dolar ->
dolar = ('https://www.google.com/search?q=dolar&oq=dolar&aqs=chrome.0.69i59l3j0i131i433i512j69i60j69i61j69i60l2.552j1j7&sourceid=chrome&ie=UTF-8')
headers = {'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
site = requests.get(dolar, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
dol = float(soup.find('span', class_='DFlfde SwHCTb').get_text().replace(",", "."))

#euro ->
euro = ('https://www.google.com/search?q=euro&oq=euro&aqs=chrome..69i57j0i131i433i512j0i433i512j46i433i512j0i433i512j69i60l3.638j1j7&sourceid=chrome&ie=UTF-8')
siteEuro = requests.get(euro, headers=headers)
soupEuro = BeautifulSoup(siteEuro.content, 'html.parser')
ur = float(soupEuro.find('span', class_='DFlfde SwHCTb').get_text().replace(",", "."))

moeda = str(input("Qual sua moeda atual (real, dolar ou euro): "))
convert = str(input("Para qual moeda deseja converter? (dolar, real ou euro)"))
valor = float(input("Qual o valor: "))

# ur = euro  and  dol = dolar

if moeda == 'real' and convert == 'dolar': #ok
    conversao = valor/dol
    print("")
    print("---------------------------------------")
    print(f"Você tem {valor} reais.")
    print(f"A quantidade em dolar é: {conversao:.2f}")
    print(f"A cotação atual do dolar é: {dol}")
    print("---------------------------------------")
    print("")
elif moeda == 'real' and convert == 'euro': #ok
    conversao = valor/ur
    print("")
    print("---------------------------------------")
    print(f"Você tem {valor} reais.")
    print(f"A quantidade em euros são: UR:{conversao:.2f}")
    print(f"A cotação atual do euro é: {ur}")
    print("---------------------------------------")
    print("")
elif moeda == 'dolar' and convert == 'real': #ok
    conversao = valor*dol
    print("")
    print("---------------------------------------")
    print(f"Você tem {valor} dolares.")
    print(f"A quantidade em reais são: R$:{conversao:.2f}")
    print(f"A cotação atual do dolar é: {dol}")
    print("---------------------------------------")
    print("")
elif moeda == 'dolar' and convert == 'euro': #ok
    acont = valor*dol
    conversao = acont/ur
    print("")
    print("---------------------------------------")
    print(f"Voçê tem {valor} dolares")
    print(f"A quantidade em euro é:{conversao:.2f}")
    print(f"A cotação atual do euro é: {ur}")
    print(f"A cotação atual do dolar é: {dol}")
    print("---------------------------------------")
    print("")
elif moeda == 'euro' and convert == 'real': 
    conversao = valor*ur
    print("")
    print("---------------------------------------")
    print(f"Você tem {valor} euros.")
    print(f"A quantidade em reais é: R${conversao:.2f}")
    print(f"A cotação atual do euro é: {ur}")
    print("---------------------------------------")
    print("")
elif moeda == 'euro' and convert == 'dolar':
    acont = valor/dol
    conversao = acont*ur
    print("")
    print("---------------------------------------")
    print(f"Você tem {valor} euros.")
    print(f"A quantidade em dolar é: {conversao:.2f}")
    print(f"A cotação atual do euro é: {ur}")
    print(f"A cotação atual do dolar é: {dol}")
    print("---------------------------------------")
    print("")
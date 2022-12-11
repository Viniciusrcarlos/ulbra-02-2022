#funções 

import requests

requisicao = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL")
print(requisicao)
dic_requisicao = requisicao.json()
print(dic_requisicao)
#cambio = dic_requisicao"USDBRL""bid"
#print(cambio)
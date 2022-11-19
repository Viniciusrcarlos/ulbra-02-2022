import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.google.com/search?q=dolar&ei=dR94Y93dJ-_f1sQPiJiFwAk&ved=0ahUKEwid7KPw-rj7AhXvr5UCHQhMAZgQ4dUDCA8&uact=5&oq=dolar&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgQIABBDMgoIABCxAxCDARBDMgQIABBDMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATIECAAQQzoECAAQAzoQCAAQgAQQsQMQgwEQRhCCAkoECEEYAEoECEYYAFAAWLkKYJEMaAFwAXgAgAGLAYgBgwOSAQMwLjOYAQCgAQHAAQE&sclient=gws-wiz-serp")

print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')
respostas = soup.find_all("span",class_="DFlfde SwHCTb")
print(respostas.text)
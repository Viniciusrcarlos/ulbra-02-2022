#Saia do loop quando x for "banana", mas dessa vez o break vem antes do print:
planetas = ["Terra", "Marte", "Vênus"]
for x in planetas:
    if x == "Vênus":
        break
    print(x)
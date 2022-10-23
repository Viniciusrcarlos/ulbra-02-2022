#Com a instrução break podemos parar o loop antes que ele tenha percorrido todos os itens:
planetas = ["Terra", "Marte", "Vênus"]
for x in planetas:
    print(x)
    if x == "Marte":
        break
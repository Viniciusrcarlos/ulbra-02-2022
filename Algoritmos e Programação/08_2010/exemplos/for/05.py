#Com a instrução continue podemos parar a iteração atual do loop e continuar com a próxima:
from re import X


planetas = ["Terra", "Marte", "Vênus"]
for x in planetas:
    if x == "Marte":
        continue
    print(x)
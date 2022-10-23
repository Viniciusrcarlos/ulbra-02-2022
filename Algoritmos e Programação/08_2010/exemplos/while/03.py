#Com a instrução continue podemos parar a iteração atual e continuar com a próxima:

i = 0
while i < 6:
    i = i + 1
    if i == 3:
        continue
    print(i)
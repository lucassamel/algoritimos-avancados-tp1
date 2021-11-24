vetor = [9, 8, 5, 3, 1, 4, 6, 7, 2]


def BubbleSort_2(lista):
    troca = True
    valor = len(lista) - 1
    while valor > 0 and troca:
        troca = False
        for i in range(valor):
            if lista[i] > lista[i + 1]:
                troca = True
                temporario = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = temporario
        valor = valor - 1


BubbleSort_2(vetor)
print(vetor)

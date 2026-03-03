valorTotal = 0

def pegarValor():
    x = int(input())
    y = int(input())

    verificarSeValoresSaoImpar(x, y)

def verificarSeValoresSaoImpar(x, y):

    for i in range(y + 1, x):
        if i % 2 != 0:
            somarValor(i)

    mostrarValor()

def somarValor(valor):
    global valorTotal
    valorTotal += valor

def mostrarValor():
    print(valorTotal)

pegarValor()
        
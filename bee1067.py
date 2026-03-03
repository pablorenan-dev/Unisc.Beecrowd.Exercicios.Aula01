def pegarValor():
    valor = int(input())

    verificarSeValorEhImpar(valor)

def verificarSeValorEhImpar(valor):

    for i in range(valor +1):
        if i % 2 != 0:
            mostrarValor(i)

def mostrarValor(valor):
    print(valor)

pegarValor()
        
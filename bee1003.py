def somar(x, y):
    soma = x + y

    return soma

def pegarValores():
    x = int(input())
    y = int(input())

    valorFinal = somar(x, y)

    mostrarValores(valorFinal)

def mostrarValores(valorFinal):
    print(f"SOMA = {valorFinal}")
    
pegarValores()

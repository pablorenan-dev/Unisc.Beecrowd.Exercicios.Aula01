def somar(x, y):
    soma = x + y

    return soma

def pegarValores():
    x = int(input())
    y = int(input())

    valorFinal = somar(x, y)

    print(f"X = {valorFinal}")
    
pegarValores()

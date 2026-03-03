def multiplicar(x, y):
    total = x * y

    return total

def pegarValores():
    x = int(input())
    y = int(input())

    valorFinal = multiplicar(x, y)

    mostrarValores(valorFinal)
    
def mostrarValores(valorFinal):
    print(f"PROD = {valorFinal}")
    
pegarValores()

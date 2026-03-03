def pegarValores():
    valor = input()

    organizarValores(valor)

def organizarValores(valor):
    valorOrganizado = valor.split()
    x = int(valorOrganizado[0])
    y = int(valorOrganizado[1])

    verificarMultiplos(x, y)

def verificarMultiplos(x, y):
    if y % x == 0 or x % y == 0:
        mostrarValores("Sao Multiplos")
    else:
        mostrarValores("Nao sao Multiplos")

def mostrarValores(resultado):
    print(resultado)

pegarValores()

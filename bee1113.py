def pegarValores():
    valor = input()

    organizarValores(valor)

def organizarValores(valor):
    valorOrganizado = valor.split()
    x = int(valorOrganizado[0])
    y = int(valorOrganizado[1])

    verificarDecrescente(x, y)

def verificarDecrescente(x, y):
    if x > y:
        mostrarValores("Decrescente")
    elif y > x:
        mostrarValores("Crescente")
    else:
        mostrarValores("")

def mostrarValores(resultado):
    print(resultado)

pegarValores()

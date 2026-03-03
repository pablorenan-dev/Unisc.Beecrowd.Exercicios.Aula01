def main():
    
    while True:
        x, y = pegarValores()

        if x == y: break

        verificarDecrescente(x, y)

def pegarValores():
    valor = input()

    return organizarValores(valor)

def organizarValores(valor):
    valorOrganizado = valor.split()
    x = int(valorOrganizado[0])
    y = int(valorOrganizado[1])

    return x, y

def verificarDecrescente(x, y):
    if x > y:
        mostrarValores("Decrescente")
    elif y > x:
        mostrarValores("Crescente")
        

def mostrarValores(resultado):
    print(resultado)

main()

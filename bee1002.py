def pegarRaio():
    raio = float(input())

    calcularAreaCirculo(raio)

def calcularAreaCirculo(raio):
    pi = 3.14159
    areaCirculo = pi * raio**2

    mostrarRaio(areaCirculo)

def mostrarRaio(areaCirculo):
    print(f"A={areaCirculo:.4f}")

pegarRaio()

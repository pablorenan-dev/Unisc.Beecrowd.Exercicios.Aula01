import math

def main():
    qntCasos = int(input())

    for i in range(qntCasos):
        x, y = pegarParametros()

        maior = verificarQualDivisor(x, y)

        print(maior)


def pegarParametros():
    valores = input().split()

    x = int(valores[0])
    y = int(valores[1])

    return x, y

def verificarQualDivisor(x, y):
    divisor = math.gcd(x, y)

    return divisor

if __name__ == "__main__":
    main()

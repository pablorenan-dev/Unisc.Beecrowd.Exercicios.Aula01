def calcularMedia(x, y):
    total = ((x * 3.5) + (y * 7.5)) / (3.5 + 7.5)

    return total

def pegarValores():
    x = float(input())
    y = float(input())

    media = calcularMedia(x, y)

    mostrarMedia(media)
    
def mostrarMedia(media):
    print(f"MEDIA = {media:.5f}")
    
pegarValores()

n = int(input())
fita = list(map(int, input().split()))

index_zeros = []

for i, valor in enumerate(fita):
    if valor == 0:
        index_zeros.append(i)

for i in index_zeros:
    aux = i
    distancia = 0
    while aux > 0 and fita[aux-1] != 0:
        aux -= 1
        distancia += 1
        if distancia >= 9:
            distancia = 9
        fita[aux] = min(fita[aux], distancia) if fita[aux] != -1 else distancia

    aux = i
    distancia = 0
    while (aux+1 < len(fita)) and fita[aux+1] != 0:
        aux += 1
        distancia += 1
        if distancia >= 9:
            distancia = 9
        fita[aux] = min(fita[aux], distancia) if fita[aux] != -1 else distancia

print(*fita)

# Esse código é lento, mas funciona >:)
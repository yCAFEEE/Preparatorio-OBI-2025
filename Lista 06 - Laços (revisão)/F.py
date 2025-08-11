d = int(input())

pontos = [0, 400, 800, 1200, 1600, 2000]
menor = 1000000000000000000000
for i in pontos:
    aux = abs(d-i)
    if aux < menor:
        menor = aux

print(menor)
n = int(input())
lista = []

for i in range(n):
    lista.append(int(input()))

cont = 0
for i in range(n):
    if i == 0:
        cont += 1
        continue
    if lista[i] != lista[i-1]:
        cont += 1
        continue
    else:
        continue

print(cont)
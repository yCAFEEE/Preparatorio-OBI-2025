n = int(input())
vet = []

for i in range(n):
    x = int(input())
    vet.append(x)

soma = 0

for i in range(n):
    primeiros_algarismos = vet[i] // 10
    ultimo_algarismo = vet[i] % 10
    soma += primeiros_algarismos ** ultimo_algarismo

print(soma)
n, saldo = map(int, input().split())
menor = 10000000000

for i in range(n):
    aux = int(input())
    saldo = saldo + aux
    if saldo < menor:
        menor = saldo

print(menor)
n = int(input())

soma_acessos = 0
dias = 1
for i in range(n):
    a = int(input())
    soma_acessos += a
    if soma_acessos < 1000000:
        dias += 1

print(dias)

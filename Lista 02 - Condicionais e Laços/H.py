n = int(input())
r = int(input())
p = int(input())

dias = 0
soma = n
while soma < p:
    soma += n * r
    n *= r
    dias += 1

print(dias)
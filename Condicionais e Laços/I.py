x = int(input())
n = int(input())

sub = 0
soma = 0
for i in range(n):
    m = int(input())
    sub = x - m
    soma += sub
soma += x
print(soma)
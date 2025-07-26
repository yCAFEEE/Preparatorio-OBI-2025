n = int(input())

m = []

for i in range(n):
    linha = list(map(int, input().split()))
    m.append(linha)

for i in range(n):
    for j in range(n):
        if m[i][j] == 0:
            idx_zero = (i+1,j+1)

sum_esperada = (n * (n**2 + 1)) / 2
soma = 0

linha_zero = idx_zero[0] - 1
soma += sum(m[linha_zero])

print(int(sum_esperada - soma))
print(idx_zero[0])
print(idx_zero[1])

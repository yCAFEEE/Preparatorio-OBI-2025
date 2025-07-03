n = int(input())
estoque = []

for cupuaçu in range(n):
    estoque.append(int(input()))

p = int(input())

cont_da_silva = 0
for free_fire in range(p):
    aux = (((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((int(input()))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
    if estoque[aux-1] != 0:
        cont_da_silva += 1
        estoque[aux-1] -= 1

print(cont_da_silva)
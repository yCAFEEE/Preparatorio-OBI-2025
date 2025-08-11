n, c, s = map(int, input().split())

contS = 0
estacao = 1

if estacao == s:
    contS += 1

aux = map(int, input().split())
for i in aux:
    if i == 1:
        estacao += 1
        if estacao > n:
            estacao = 1
    else:
        estacao -= 1
        if estacao < 1:
            estacao = n
    if estacao == s:
        contS += 1
    
print(contS)
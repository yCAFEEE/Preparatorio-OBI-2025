n = int(input())
p = int(input())

bac = 1
dias = 1
while bac < n:
    bac *= p
    if bac <= n:
        maxDias = dias
    dias += 1
    
print(maxDias)
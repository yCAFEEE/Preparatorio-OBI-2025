muro = int(input())
sobe = int(input())
desce = int(input())

dias = 0
while muro > 0:
    muro -= sobe
    if(muro <= 0): 
        dias += 1
        break
    muro += desce
    dias += 1

print(dias)
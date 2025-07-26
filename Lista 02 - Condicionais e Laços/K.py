n = int(input())

val_i = list(map(int, input().split()))[:n]

lamA = 0
lamB = 0
for i in val_i:
    if i == 1:
        lamA = not lamA
    else:
        lamA = not lamA
        lamB = not lamB


lamA = int(lamA)
lamB = int(lamB)
print(lamA)
print(lamB)
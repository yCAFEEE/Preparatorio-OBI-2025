vit = 0
for i in range(6):
    result = input()
    if result == 'V':
        vit += 1

if vit >= 5:
    print(1)
elif vit >= 3 and vit < 5:
    print(2)
elif vit >= 1 and vit < 3:
    print(3)
else:
    print(-1)
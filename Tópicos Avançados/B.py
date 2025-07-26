n = int(input())
figuras = {i for i in range(1, n+1)}
m = int(input())

for i in range(m):
    x = int(input())
    figuras.discard(x)

print(len(figuras))
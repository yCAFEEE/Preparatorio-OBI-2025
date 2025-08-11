n = int(input())

e = []
a = []
g = []

for i in range(n):
    entrada = input().split()
    e.append(entrada[0])
    a.append(float(entrada[1]))
    g.append(float(entrada[2]))

nada = True
for i in range(n):
    if a[i] <= (g[i] * 0.7):
        print(e[i])
        nada = False

if nada:
    print("*")
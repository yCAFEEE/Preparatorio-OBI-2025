n = int(input())
lamp = []

for i in range(n):
    lamp.append(int(input()))

cont = 0
max_cont = 0
for i in range(n):
    if lamp[i] + lamp[(i+1) % n] < 1000:
        cont += 1
        max_cont = max(max_cont, cont)
    else:
        cont = 0

print(max_cont)
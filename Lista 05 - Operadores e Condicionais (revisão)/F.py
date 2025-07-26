t1 = int(input())
t2 = int(input())
t3 = int(input())

tempos = [t1, t2, t3]

pos = list(enumerate(tempos, start=1))
pos_ordenada = sorted(pos, key=lambda x : x[1])

for i, bomba in pos_ordenada:
    print(i)
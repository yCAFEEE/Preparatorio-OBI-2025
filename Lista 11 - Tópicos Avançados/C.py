a = int(input())
b = int(input())
c = int(input())
d = int(input())

vet = [a, b, c, d]
vet.sort()

t1 = vet[0] + vet[3]
t2 = vet[1] + vet[2]

print(abs(t1-t2))
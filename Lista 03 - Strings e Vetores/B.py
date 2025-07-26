n, c = map(int, input().split())
vet = list(map(int, input().split()))[:n]

vet.sort(reverse=True)
print(vet[c-1])
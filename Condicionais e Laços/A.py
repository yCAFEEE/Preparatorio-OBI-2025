a = int(input())
b = int(input())
c = int(input())
h = int(input())
l = int(input())

pares = [(a,b), (a,c), (b,c)]

for x, y in pares:
    if(x <= l and y <= h) or (x <= h and y <= l):
        print("S")
        exit(0)
print("N")
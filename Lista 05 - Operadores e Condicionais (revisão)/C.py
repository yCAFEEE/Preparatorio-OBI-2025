a, b = map(int, input().split())

c1 = 2*a - b
c2 = (a + b) / 2
c3 = 2*b - a

print(min(c1, c2, c3))
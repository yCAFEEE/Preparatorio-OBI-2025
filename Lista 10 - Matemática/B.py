h, p, f, d = map(int, input().split())

if p > f:
    d_policial = p-f
else:
    d_policial = f-p

if h > f:
    d_heli = h-f
else:
    d_heli = f-h

print(d_heli, d_policial)
l, r, d = map(int, input().split())

if r > 50 and l < r and r > d:
    print("S")
else:
    print("N")
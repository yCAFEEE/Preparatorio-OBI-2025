def solve(h, p, f, d):
    pos = f
    while True:
        if pos == h:
            return 'S'
        if pos == p:
            return 'N'
        pos = (pos + d) % 16

h, p, f, d = map(int, input().split())

print(solve(h, p, f, d))
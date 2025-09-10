import math

n, m = map(int, input().split())

while math.gcd(n, m) != 1:
    m -= 1

print(m)
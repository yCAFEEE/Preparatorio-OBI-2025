n = int(input())
g = int(input())
m = int(input())

total_g = g*8
total_m = m*6

if total_g + total_m <= n:
    print(0)
else:
    print((total_g + total_m) - n)
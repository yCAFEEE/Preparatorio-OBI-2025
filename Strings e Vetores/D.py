n = int(input())
a = list(map(int, input().split()))[:n]

ta_certo = True
l = 0
r = n-1
while(l != n-1 and r != 0):
    soma1 = a[l] + a[r]
    soma2 = a[l+1] + a[r-1]
    if soma1 == soma2:
        l += 1
        r -= 1
    else:
        ta_certo = False
        break

print("S" if ta_certo else "N")
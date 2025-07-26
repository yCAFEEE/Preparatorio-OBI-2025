p1, c1, p2, c2 = input().split(" ")
p1 = int(p1)
c1 = int(c1)
p2 = int(p2)
c2 = int(c2)
l1 = p1 * c1
l2 = p2 * c2

if l1 == l2:
    print(0)
elif l1 < l2:
    print(1)
else:
    print(-1)
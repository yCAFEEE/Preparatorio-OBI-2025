p, r = input().split(" ")
p = int(p)
r = int(r)
if not p:
    print("C")
elif p and not r:
    print("B")
else:
    print("A")
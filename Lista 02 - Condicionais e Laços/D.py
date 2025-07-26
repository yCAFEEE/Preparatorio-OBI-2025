a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a == b + c + d and d == b + c and b == c:
    print("S")
else:
    print("N")
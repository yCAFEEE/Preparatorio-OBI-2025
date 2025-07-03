p = int(input())
d1 = int(input())
d2 = int(input())
sum = d1 + d2

if not p and sum % 2 == 0:
    print(0)

elif not p and sum % 2 != 0:
    print(1)

elif p and sum % 2 == 0:
    print(1)

else:
    print(0)
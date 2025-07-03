n = int(input())

tamP = 0
tamM = 0
val_t = list(map(int, input().split()))[:n]

for t in val_t:
    if t == 1:
        tamP += 1
    else:
        tamM += 1

prodP = int(input())
prodM = int(input())

if tamP == prodP and tamM == prodM:
    print("S")
else:
    print("N")
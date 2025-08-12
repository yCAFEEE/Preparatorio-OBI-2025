k, m = map(int, input().split())
alfa = input()
str = input()

set_alfa = set(alfa)

for i in str:
    if i not in set_alfa:
        print("N")
        exit()
        
print("S")
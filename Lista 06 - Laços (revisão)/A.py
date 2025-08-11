n = int(input())

aux = input()

a = False
b = False
c = False

if aux == 'A':
    a = True

elif aux == 'B':
    b = True

else:
    c = True

for i in range(n):
    comando = int(input())
    if comando == 1:
        aux = a
        a = b
        b = aux
    elif comando == 2:
        aux = c
        c = b
        b = aux
    else:
        aux = c
        c = a
        a = aux

if a:
    print("A")

elif b:
    print("B")

else:
    print("C")

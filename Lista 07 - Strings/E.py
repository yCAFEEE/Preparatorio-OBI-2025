n = int(input())
str = input()

resp = ''
cont = 1
for i in range(1, len(str)):
    if str[i] == str[i-1]:
        cont += 1
    else:
        resp += f"{cont} {str[i-1]} "
        cont = 1
resp += f"{cont} {str[-1]}"
print(resp)
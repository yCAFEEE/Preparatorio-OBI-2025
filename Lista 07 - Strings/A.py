n = int(input())
str = input()

str = str.replace(' ', '')

cont100 = 0
for i in range(n-2):
    if str[i] == '1' and str[i+1] == '0' and str[i+2] == '0':
        cont100 += 1

print(cont100)
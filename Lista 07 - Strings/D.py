n = int(input())

str1 = input()
str2 = input()

str1 = str1.replace(' ', '').replace(',', '').replace('.', '')
str2 = str2.replace(' ', '').replace(',', '').replace('.', '')

if sorted(str1) == sorted(str2):
    print("S")
else:
    print("N")
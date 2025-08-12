alfa = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'z'}

str = input()

str = str.replace(' ', '').replace(':', '').replace(',', '')

s = set(str)
if all(letter in s for letter in alfa):
    print("S")
else:
    print("N")
n = int(input())
id_pessoa = list(map(int, input().split()))

m = int(input())
id_pessoa_sai = set(map(int, input().split()))

for i in id_pessoa_sai:
    if i in id_pessoa:
        id_pessoa.remove(i)

print(*id_pessoa)
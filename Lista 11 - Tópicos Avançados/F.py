def insatisfeito(i, func, sub):
    salario_atual = func[i][1]
    for s in sub[i]:
        if func[s][1] > salario_atual:
            return True
    return False

n = int(input())

func = []

for i in range(n):
    c, s = map(int, input().split())
    func.append((c, s))

sub = [[] for _ in range(n)]
for i in range(n):
    chefe = func[i][0] - 1
    if chefe != i:
        sub[chefe].append(i)

insatis = [insatisfeito(_, func, sub) for _ in range(n)]

a = int(input())
conts = []

conts.append(insatis.count(True))
for i in range(a):
    f, s_r = map(int, input().split())
    chefe = func[f-1][0] - 1
    func[f-1] = (func[f-1][0], s_r)

    for j in [f-1, chefe]:
        if 0 <= j < n:
            insatis[j] = insatisfeito(j, func, sub)
    conts.append(insatis.count(True))


print('\n'.join(map(str, conts)))
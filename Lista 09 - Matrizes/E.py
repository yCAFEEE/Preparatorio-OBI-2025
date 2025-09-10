def solve(n):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            top_dist = i + 1
            bottom_dist = n - i
            left_dist = j + 1
            right_dist = n - j

            val = min(top_dist, bottom_dist, left_dist, right_dist)
            linha.append(val)
        matriz.append(linha)
    for linha in matriz:
        print(*linha)

n = int(input())
solve(n)
k = int(input())
l = int(input())

fases = ["oitavas", "quartas", "semifinal", "final"]
rodadas = 0

while k != l:
    k = (k+1) // 2
    l = (l+1) // 2
    rodadas += 1

print(fases[rodadas-1])
n, m = map(int, input().split())

field = [[0] + list(map(int, input().split())) for _ in range(n)]
field.insert(0, [0] * (m + 1))

for i in range(1, n + 1):
    for j in range(1, m + 1):
        field[i][j] = max(field[i - 1][j], field[i][j - 1]) + field[i][j]

print(field[-1][-1])

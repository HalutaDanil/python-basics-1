with open("input.txt") as file:
    table = [line.split() for line in file]

rows = len(table)
cols = len(table[0])
used = [[False] * cols for _ in range(rows)]


def dfs(r, c, cells):
    used[r][c] = True
    cells.append((r, c))
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if (
            0 <= nr < rows
            and 0 <= nc < cols
            and not used[nr][nc]
            and table[nr][nc] == "1"
        ):
            dfs(nr, nc, cells)


count_quad, count_circ = 0, 0
for i in range(rows):
    for j in range(cols):
        if used[i][j] or table[i][j] != "1":
            continue
        cells = []
        dfs(i, j, cells)
        min_r = min(r for r, c in cells)
        max_r = max(r for r, c in cells)
        min_c = min(c for r, c in cells)
        max_c = max(c for r, c in cells)
        h = max_r - min_r + 1
        w = max_c - min_c + 1
        if h == w and len(cells) == h * w:
            count_quad += 1
        else:
            count_circ += 1

print(count_quad, count_circ)

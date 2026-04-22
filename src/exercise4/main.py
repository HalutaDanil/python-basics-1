import sys

count_line = input()

if not (count_line.isdigit()) or count_line == "0":
    print("Natural number was expected")
    sys.exit(1)

count_line = int(count_line)

pascal_triangle = [[0] * i for i in range(1, count_line + 1)]

for i in range(count_line):
    pascal_triangle[i][0], pascal_triangle[i][-1] = 1, 1
    for j in range(1, len(pascal_triangle[i]) - 1):
        pascal_triangle[i][j] = (
            pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j]
        )

for i in range(len(pascal_triangle)):
    for j in range(len(pascal_triangle[i])):
        print(pascal_triangle[i][j], end=" ")
    print()

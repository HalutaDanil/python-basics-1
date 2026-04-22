import sys

param = input().split()

if len(param) != 2:
    print("incorrect input")
    sys.exit(1)

if not param[0].isdigit() or not param[1].isdigit():
    print("incorrect input")
    sys.exit(1)

param = list(map(int, param))

if param[0] < 2 or param[1] <= 0:
    print("incorrect input")
    sys.exit(1)

shop = []
for _ in range(param[0]):
    position = input().split()

    if len(position) != 3:
        print("incorrect input")
        sys.exit(1)

    if (
        not position[0].isdigit()
        or not position[1].isdigit()
        or not position[2].isdigit()
    ):
        print("incorrect input")
        sys.exit(1)

    year, cost, time = map(int, position)

    if year <= 0 or cost <= 0 or time <= 0:
        print("incorrect input")
        sys.exit(1)

    shop.append([year, cost, time])

best = None

for i in range(len(shop)):
    for j in range(i + 1, len(shop)):
        if shop[i][0] == shop[j][0] and shop[i][2] + shop[j][2] == param[1]:
            total_cost = shop[i][1] + shop[j][1]
            if best is None or total_cost < best:
                best = total_cost

print(best)


p = []
for i in range(4):
    p.append(list(map(int, input().split())))


def color(plate, p):
    for i in range(p[0], p[2]):
        for j in range(p[1], p[3]):
            plate[i][j] = 1

plate = [[0] * 100 for i in range(100)]

for i in range(4):
    color(plate, p[i])
ans = 0
for i in range(len(plate)):
    ans += sum(plate[i])
print(ans)

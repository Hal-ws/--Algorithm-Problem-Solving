import sys

T = int(sys.stdin.readline())
for i in range(T):
    n = int(sys.stdin.readline())
    cloths = []
    for j in range(n):
        name, group = map(str, sys.stdin.readline().split())
        cloths.append([group, name])
    cloths = sorted(cloths)
    category = [0]
    for j in range(0, len(cloths)):
        if cloths[j][0] == cloths[j - 1][0]:
            category[len(category) - 1] += 1
        else:
            category.append(1)
    ans = 1
    for j in range(len(category)):
        ans *= (category[j] + 1)
    else:
        print(ans - 1)

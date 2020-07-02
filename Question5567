import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

relations = [0] * m
for i in range(m):
    relations[i] = list(map(int, sys.stdin.readline().split()))

friends = []
for i in range(m):
    if relations[i][0] == 1:
        friends.append(relations[i][1])
    if relations[i][1] == 1:
        friends.append(relations[i][0])

friends = list(set(friends))
l = len(friends)
fOfF = []
for i in range(l):
    for j in range(m):
        if friends[i] == relations[j][0] and relations[j][1] != 1:
            fOfF.append(relations[j][1])
        if friends[i] == relations[j][1] and relations[j][0] != 1:
            fOfF.append(relations[j][0])
ans = set(friends + fOfF)
print(len(ans))

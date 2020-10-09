N, M = map(int, input().split())
num = list(map(int, input().split()))

move = 0
place = []
for i in range(len(num)):
    place.append([num[i] - 1, N - num[i]])
for i in range(len(num)):
    if place[i][0] < place[i][1] + 1: ## move to left
        move += (place[i][0])
        if i < len(num) - 1:
            for j in range(i + 1, len(num)):
                if place[j][0] > place[i][0]:
                    place[j][0] -= (place[i][0] + 1)
                    place[j][1] += (place[i][0])
                else:
                    place[j][0] = place[j][0] + place[i][1]
                    place[j][1] = place[j][1] - place[i][1] - 1
    else:
        move += (place[i][1] + 1)
        if i < len(num) - 1:
            for j in range(i + 1, len(num)):
                if place[j][0] < place[i][0]:
                    place[j][1] -= (place[i][1] + 1)
                    place[j][0] += (place[i][1])
                else:
                    place[j][0] = place[j][0] - place[i][0] - 1
                    place[j][1] = place[j][1] + place[i][0]

print(move)

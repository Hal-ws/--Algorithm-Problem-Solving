N = int(input())

people = []
i = 0
while(i < N):
    people.append(list(map(int, input().split())))
    i += 1

rankList = []
i = 0
while(i < len(people)):
    rank = 1
    j = 0
    while(j < len(people)):
        if(people[i][0] < people[j][0] and people[i][1] < people[j][1]):
            rank += 1
        j += 1
    rankList.append(rank)
    i += 1

for j in range(len(rankList)):
    print(rankList[j], end = ' ')

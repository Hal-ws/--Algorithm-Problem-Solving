import itertools

N = int(input())
teamNumber = N // 2

def get_stat_sum(memberList, stat):
    sum = 0
    temp = list(itertools.combinations(memberList, 2))
    for i in range(len(temp)):
        sum += stat[temp[i][0]][temp[i][1]]
        sum += stat[temp[i][1]][temp[i][0]]
    return sum

stat = []
for i in range(N):
    stat.append(list(map(int, input().split())))
memberList = []
for i in range(N):
    memberList.append(i)

startMemberList = list(itertools.combinations(memberList, N // 2))
statSumDifference = -1
for i in range(len(startMemberList)):
    startTeam = startMemberList[i]
    linkTeam = []
    for j in range(N):
        if j not in startTeam:
            linkTeam.append(j)
    tempList = [get_stat_sum(startTeam, stat), get_stat_sum(linkTeam, stat)]
    temp = max(tempList) - min(tempList)
    if statSumDifference == -1:
        statSumDifference = temp
    elif temp <= statSumDifference:
        statSumDifference = temp
print(str(statSumDifference))

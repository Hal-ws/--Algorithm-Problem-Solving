import sys
N = int(input())

peopleNum = []
peopleName = []
for i in range(N):
    ageAndName = list(sys.stdin.readline().split())
    peopleNum.append([int(ageAndName[0]), i]) ## 나이와 가입순서 기입
    peopleName.append(ageAndName[1])
peopleNum = sorted(peopleNum)
for i in range(N):
    print(str(peopleNum[i][0]) + ' ' + str(peopleName[peopleNum[i][1]]))

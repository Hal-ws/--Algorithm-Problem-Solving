import sys

T = int(sys.stdin.readline())

def havingTest():
    N = int(sys.stdin.readline())
    people = []
    for i in range(N):
        a, b = map(int, sys.stdin.readline().split())
        people.append([a, b])
    people = sorted(people)
    bestInterview = people[0][1]
    ans = 1
    for i in range(1, N):
        if people[i][1] < bestInterview:
            bestInterview = people[i][1]
            ans += 1
    print(ans)


for i in range(T):
    havingTest()

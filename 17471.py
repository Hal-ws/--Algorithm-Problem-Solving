import sys
from collections import deque
from itertools import combinations



def main():
    N = int(sys.stdin.readline())
    people = [0] + list(map(int, sys.stdin.readline().split()))
    near = [[]]
    for i in range(N):
        temp = list(map(int, sys.stdin.readline().split()))
        near.append(temp[1:temp[0] + 1])
    diff = 10000
    for i in range(1, N): #1:N - 1부터 N - 1: 1로 쪼개는경우
        temp = seperate(N, people, near, i, N - i)
        if temp <= diff:
            diff = temp
    if diff == 10000:
        print(-1)
    else:
        print(diff)


def seperate(N, people, near, nA, nB):#nA, nB개의 그룹 A, B로 쪼갠후 차이를 구하는 함수로 넘겨줌
    city = [(i + 1) for i in range(N)]
    A = list(combinations(city, nA)) # A[i]번 케이스와 B[l - i - 1]번 케이스를 구별한다.
    B = list(combinations(city, nB))
    l = len(A)
    result = 10000
    for i in range(l):
        if connetchk(A[i], near, N) and connetchk(B[l - i - 1], near, N): #
            temp = getdiff(A[i], B[l - i - 1], people)
            if temp <= result:
                result = temp
    return result #분리 가능해서 result에 저장할 수 있는 값이 없으면 10000.


def connetchk(group, near, N): #그룹이 다 연결됐는지 확인
    chk = [0] * (N + 1)
    q = deque()
    q.append(group[0])
    chk[group[0]] = 1
    while len(q) > 0:
        nearcities = near[q[0]] #현재 보고 있는 도시와 연결된 도시들 list
        ln = len(nearcities)
        for i in range(ln):
            if chk[nearcities[i]] == 0 and nearcities[i] in group:
                chk[nearcities[i]] = 1
                q.append(nearcities[i])
        q.popleft()
    lg = len(group)
    for i in range(lg): #해당 그룹에 있는 도시들은 다 방문했는지 확인
        if chk[group[i]] == 0:
            return 0 #방문안된 애가 있으면 끊긴거임
    return 1 # 연결됐으면 1


def getdiff(A, B, people):
    Apeople, Bpeople = 0, 0
    lA, lB = len(A), len(B)
    for i in range(lA):
        Apeople += people[A[i]]
    for i in range(lB):
        Bpeople += people[B[i]]
    return abs(Apeople - Bpeople)


if __name__ == "__main__":
    main()

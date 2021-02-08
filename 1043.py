import sys
from collections import deque


def main():
    N, M = map(int, sys.stdin.readline().split())
    truths = list(map(int, sys.stdin.readline().split()))
    truChk = [0] * M # 진실을 말할 파티에 1 표시
    personChk = [0] * (N + 1) # 체크한사람 표시
    truths = truths[1:]
    q = deque()
    for p in truths:
        q.append(p)
        personChk[p] = 1
    parties = []
    for i in range(M):
        party = list(map(int, sys.stdin.readline().split()))
        parties.append(party[1:])
    while len(q) > 0:
        person = q[0]
        for pIdx in range(M):
            party = parties[pIdx]
            if person in party: # 진실을 아는 사람이 party에 있음
                truChk[pIdx] = 1
                for member in party:
                    if personChk[member] == 0:
                        personChk[member] = 1
                        q.append(member)
        q.popleft()
    print(M - sum(truChk))


if __name__ == '__main__':
    main()

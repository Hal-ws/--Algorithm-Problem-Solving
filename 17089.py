import sys


def main():
    N, M = map(int, sys.stdin.readline().split())
    cntList = [0] * (N + 1)
    relations = [[] for i in range(N + 1)]
    connectChk = [[0 for j in range(N + 1)] for i in range(N + 1)]
    answer = 12001
    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())
        relations[a].append(b)
        relations[b].append(a)
        connectChk[a][b] = 1
        connectChk[b][a] = 1
        cntList[a] += 1
        cntList[b] += 1
    for first in range(1, N + 1):
        for second in relations[first]: # 2번째 친구
            for third in relations[second]:
                if connectChk[third][first]: # 3-1 번도 친구
                    tmp = cntList[first] + cntList[second] + cntList[third] - 6
                    if tmp < answer:
                        answer = tmp
    if answer == 12001:
        print(-1)
    else:
        print(answer)


if __name__ == '__main__':
    main()

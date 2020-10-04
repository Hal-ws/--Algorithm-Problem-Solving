import sys

def main():
    N = int(sys.stdin.readline())
    players = [None] * N
    for i in range(N):
        players[i] = sys.stdin.readline()
    players = sorted(players)
    cnt = 1
    std = players[0][0]
    ans = []
    i = 1
    while i < N:
        if players[i][0] == std:
            cnt += 1
        else:
            cnt = 1
            std = players[i][0]
        if cnt == 5:
            ans.append(players[i][0])
            for j in range(i, N):
                if players[j][0] != std:
                    std = players[j][0]
                    i = j
                    cnt = 1
                    break
        i += 1
    l = len(ans)
    if l > 0:
        for i in range(l):
            print(ans[i], end = '')
    else:
        print("PREDAJA")


if __name__ == '__main__':
    main()

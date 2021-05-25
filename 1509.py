from collections import deque


def main():
    word = input()
    l = len(word)
    dp = [[0 for j in range(l)] for i in range(l)]
    connect = [[] for i in range(l)] # i번 idx 로 시작할때 팰린드롬인것들 등록
    visit = [l + 2 for i in range(l)]
    answer = l
    q = deque()
    for pl in range(1, l + 1):
        for s in range(l): #
            e = s + pl - 1
            if e >= l:
                break
            if s == e:
                dp[s][e] = 1
            elif s + 1 == e and word[s] == word[e]:
                dp[s][e] = 1
            else:
                if dp[s + 1][e - 1] == 1 and word[s] == word[e]:
                    dp[s][e] = 1
            if dp[s][e]:
                connect[s].append(e)

    for endP in connect[0]:
        q.append([endP, 1]) # 현재 끝나는 위치, 분할된 갯수
        visit[endP] = 1
    while len(q) > 0:
        tmp = q.popleft()
        endP, cnt = tmp[0], tmp[1]
        if endP == l - 1:
            if cnt < answer:
                answer = cnt
        else:
            sP = endP + 1
            for nEnd in connect[sP]:
                if cnt + 1 < visit[nEnd]:
                    q.append([nEnd, cnt + 1])
                    visit[nEnd] = cnt + 1
    print(answer)


if __name__ == '__main__':
    main()

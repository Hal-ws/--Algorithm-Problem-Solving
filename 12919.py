from collections import deque


def main():
    S = input()
    T = input()
    print(bfs(T, S))


def bfs(word, target):
    visit = set()
    visit.add(word)
    tAcnt = target.count('A')
    tBcnt = target.count('B')
    ansL = len(target)
    q = deque()
    q.append([word, word.count('A'), word.count('B'), len(word)])
    while len(q) > 0:
        w, aCnt, bCnt, l = q[0][0], q[0][1], q[0][2], q[0][3]
        if w == target:
            return 1
        if aCnt > tAcnt and w[l - 1] == 'A' and w[:l - 1] not in visit and l > ansL:#끝의 A를 빼줌
            q.append([w[:l - 1], aCnt - 1, bCnt, l - 1])
        if bCnt > tBcnt and w[0] == 'B':
            w = w[1:]
            w = w[::-1]
            if w not in visit and l > ansL:
                q.append([w, aCnt, bCnt - 1, l - 1])
        q.popleft()
    return 0


if __name__ == '__main__':
    main()

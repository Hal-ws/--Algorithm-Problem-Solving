from collections import deque


def main():
    N = int(input())
    cases = [1, 5, 10, 50]
    q = deque(cases)
    for i in range(2, N + 1):
        possibles = [0] * 1001
        lq = len(q)
        for j in range(lq):
            for k in range(4):
                if possibles[q[0] + cases[k]] == 0:
                    possibles[q[0] + cases[k]] = 1
                    q.append(q[0] + cases[k])
            q.popleft()
    if N != 1:
        print(sum(possibles))
    else:
        print(4)


if __name__ == "__main__":
    main()

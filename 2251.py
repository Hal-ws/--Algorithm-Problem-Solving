from collections import deque


def main():
    A, B, C = map(int, input().split())
    q = deque()
    q.append([0, 0, C])
    chk = [[-1 for i in range(B + 1)] for j in range(A + 1)]
    chk[0][0] = C
    while len(q) > 0:
        if q[0][0] > 0: # A를 붓는다
            if q[0][1] < B: # B에 붓는다
                temp = pour(0, 1, 2, q, B)
                if chk[temp[0]][temp[1]] == -1:
                    chk[temp[0]][temp[1]] = temp[2]
                    q.append(temp)
            if q[0][2] < C: # C에 붓는다
                temp = pour(0, 2, 1, q, C)
                if chk[temp[0]][temp[1]] == -1:
                    chk[temp[0]][temp[1]] = temp[2]
                    q.append(temp)
        if q[0][1] > 0: # B를 붓는다
            if q[0][0] < A:
                temp = pour(1, 0, 2, q, A)
                if chk[temp[0]][temp[1]] == -1:
                    chk[temp[0]][temp[1]] = temp[2]
                    q.append(temp)
            if q[0][2] < C:
                temp = pour(1, 2, 0, q, C)
                if chk[temp[0]][temp[1]] == -1:
                    chk[temp[0]][temp[1]] = temp[2]
                    q.append(temp)
        if q[0][2] > 0:
            if q[0][0] < A:
                temp = pour(2, 0, 1, q, A)
                if chk[temp[0]][temp[1]] == -1:
                    chk[temp[0]][temp[1]] = temp[2]
                    q.append(temp)
            if q[0][1] < B:
                temp = pour(2, 1, 0, q, B)
                if chk[temp[0]][temp[1]] == -1:
                    chk[temp[0]][temp[1]] = temp[2]
                    q.append(temp)
        q.popleft()
    ansList = sorted(chk[0])
    for i in range(B + 1):
        if ansList[i] != -1:
            print(ansList[i], end=' ')
    return 0


def pour(s, e, n, q, M): ## s index에 있는걸 e index 로 붓는다. n은 상관없는 index M: e index가 저장가능한 용량
    temp = [0, 0, 0]
    if q[0][s] < M - q[0][e]: # 있는거 다 부어버릴수 있음
        temp[s] = 0
        temp[e] = q[0][e] + q[0][s]
    else: # 있는거 다부으면 넘침
        temp[e] = M
        temp[s] = q[0][s] - (M - q[0][e])
    temp[n] = q[0][n]
    return temp


if __name__ == "__main__":
    main()

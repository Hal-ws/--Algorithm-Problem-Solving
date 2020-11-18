from collections import deque


def main():
    A, B, C = map(int, input().split())
    water = [0, 0, C]
    q = deque()
    q.append([0, 0, C])
    chk = [[0] for i in range(B + 1) for j in range(A + 1)]
    chk[0][0] = C
    while len(q) > 0:
        if q[0][0] > 0:
            if q[0][1] < B: # B에 부음
                if q[0][0] > B - q[0][1]: # B에 다 붓고도 남음
                    if chk[q[0][0] - B + q[0][1]][B] == 0:
                        chk[q[0][0] - B + q[0][1]][B] = q[0][2]
                        q.append(q[0][0] - B + q[0][1], B, q[0][2])
                else: #남는거 다부음
                    if chk[0][q[0][1] + q[0][0]] == 0:
                        chk[0][q[0][1] + q[0][0]] = q[0][2]
                        q.append([0, q[0][1] + q[0][0], q[0][2]])
            if q[0][2] < C: # C에부음
                if q[0][0] > C - q[0][2]:
                    if chk[q[0][0] - C + q[0][2]][q[0][1]] == 0:
                        chk[q[0][0] - C + q[0][2]][q[0][1]] = C
                        q.append([q[0][0] - C + q[0][2], q[0][1], C])
                else:
                    if chk[0][q[0][1]] == 0:
                        chk[0][q[0][1]] = q[0][2] + q[0][0]
                        q.append([0, q[0][1], q[0][2] + q[0][0]])
        if q[0][1] > 0:
            if q[0][0] < A:
                if q[0][1] > A - q[0][0]:
                    if chk[A][q[0][1] - A + q[0][0]] == 0:
                        chk[A][q[0][1] - A + q[0][0]] = q[0][2]
                        q.append([A, q[0][1] - A + q[0][0], q[0][2]])
                else:
                    if chk[q[0][0] + q[0][1]][0] == 0:
                        chk[q[0][0] + q[0][1]][0] = q[0][2]
                        q.append([q[0][0] + q[0][1], 0, q[0][2]])
            if q[0][2] < C:
                if q[0][1] > C - q[0][2]:
                    if chk[q[0][0]][q[0][1] - C + q[0][2]] == 0:
                        chk[q[0][0]][q[0][1] - C + q[0][2]] = C
                        q.append([q[0][0], q[0][1] - C + q[0][2], C])
                else:
                    if chk[q[0][0]][0] == 0:
                        chk[q[0][0]][0] = q[0][2] + q[0][1]
                        q.append([q[0][0], 0, q[0][2] + q[0][1]])
        if q[0][2] > 0:
            if q[0][0] < A:
                if q[0][2] > A - q[0][0]:
                    if chk[A][q[0][1]] == 0:
                        chk[A][q[0][1]] = q[0][2] - A + q[0][0]
                        q.append([A, q[0][1], q[0][2] - A + q[0][0]])
                else:
                    if chk[q[0][0] + q[0][2]][q[0][1]] == 0:
                        chk[q[0][0] + q[0][2]][q[0][1]] = 0
                        q.append([q[0][0] + q[0][2], q[0][1], 0])
        q.popleft()
    print(chk[0])


if __name__ == "__main__":
    main()

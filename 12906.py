from collections import deque


def main():
    pillars = ['', '', '']
    q = deque()
    visit = set()
    for i in range(3):
        a = input()
        if a[0] != '0':
            if a[1] == ' ':
                pillars[i] = a[2:]
            else:
                pillars[i] = a[3:]
    visit.add(pillars[0] + pillars[1] + pillars[2] + str(len(pillars[0])) + str(len(pillars[1])))
    q.append(pillars + [len(pillars[0]), len(pillars[1]), len(pillars[2]), 0])
    while len(q) > 0:
        p0, p1, p2, l0, l1, l2, cnt = q[0][0], q[0][1], q[0][2], q[0][3], q[0][4], q[0][5], q[0][6]
        flag = 1
        for i in range(l0):
            if p0[i] != 'A':
                flag = 0
                break
        for i in range(l1):
            if p1[i] != 'B':
                flag = 0
                break
        for i in range(l2):
            if p2[i] != 'C':
                flag = 0
                break
        if flag:
            ans = cnt
            break
        if l0 > 0: #p0에서 뺄게 있을때
            np0 = p0[:l0 - 1]
            np1 = p1 + p0[l0 - 1]
            np2 = p2 + p0[l0 - 1]
            chk0 = np0 + np1 + p2 + str(l0 - 1) + str(l1 + 1) # 0->1
            chk1 = np0 + p1 + np2 + str(l0 - 1) + str(l1) #0->2
            if chk0 not in visit:
                q.append([np0, np1, p2, l0 - 1, l1 + 1, l2, cnt + 1])
                visit.add(chk0)
            if chk1 not in visit:
                q.append([np0, p1, np2, l0 - 1, l1, l2 + 1, cnt + 1])
                visit.add(chk1)
        if l1 > 0: #p1에서 옮길게 있을때
            np0 = p0 + p1[l1 - 1]
            np1 = p1[:l1 - 1]
            np2 = p2 + p1[l1 - 1]
            chk0 = np0 + np1 + p2 + str(l0 + 1) + str(l1 - 1) #1->0
            chk1 = p0 + np1 + np2 + str(l0) + str(l1 - 1) #1->2
            if chk0 not in visit:
                q.append([np0, np1, p2, l0 + 1, l1 - 1, l2, cnt + 1])
                visit.add(chk0)
            if chk1 not in visit:
                q.append([p0, np1, np2, l0, l1 - 1, l2 + 1, cnt + 1])
                visit.add(chk1)
        if l2 > 0: #p2에서 옮김
            np0 = p0 + p2[l2 - 1]
            np1 = p1 + p2[l2 - 1]
            np2 = p2[:l2 - 1]
            chk0 = np0 + p1 + np2 + str(l0 + 1) + str(l1) #2->0
            chk1 = p0 + np1 + np2 + str(l0) + str(l1 + 1) #2->1
            if chk0 not in visit:
                q.append([np0, p1, np2, l0 + 1, l1, l2 - 1, cnt + 1])
                visit.add(chk0)
            if chk1 not in visit:
                q.append([p0, np1, np2, l0, l1 + 1, l2 - 1, cnt + 1])
                visit.add(chk1)
        q.popleft()
    print(ans)


if __name__ == '__main__':
    main()

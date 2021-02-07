import sys


def main():
    global connect, visit, farDis, farNode1, farNode2
    V = int(sys.stdin.readline())
    connect = [[] for j in range(V + 1)]
    visit = [0] * (V + 1)
    farDis, farNode1, farNode2 = 0, 0, 0
    for i in range(V):
        tmp = list(map(int, sys.stdin.readline().split()))
        node = tmp[0]
        connect[node] = tmp[1:len(tmp) - 1]
    visit[1] = 1
    getfar(1, 0, 1)
    visit[1] = 0
    farDis = 0
    visit[farNode1] = 1
    getfar(farNode1, 0, 2)
    visit[farNode1] = 0
    print(farDis)




def getfar(node, r, flag): # flag: 1 -> farNode1 구함, 2일때 -> farNode2 구함
    global connect, visit, farDis, farNode1, farNode2
    for nIdx in range(0, len(connect[node]), 2):
        nxt = connect[node][nIdx]
        dis = connect[node][nIdx + 1]
        if visit[nxt] == 0:
            visit[nxt] = 1
            getfar(nxt, r + dis, flag)
            visit[nxt] = 0
    if farDis < r:
        farDis = r
        if flag == 1:
            farNode1 = node
        else:
            farNode2 = node


if __name__ == '__main__':
    main()

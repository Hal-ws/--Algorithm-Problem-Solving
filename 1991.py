import sys


def main():
    global N, cnt1, cnt2, cnt3, word1, word2, word3
    cnt1, cnt2, cnt3 = 0, 0, 0
    word1, word2, word3 = '', '', ''
    N = int(sys.stdin.readline())
    tree = [[None, None, None] for i in range(N)]
    for i in range(N):
        parent, left, right = map(str, sys.stdin.readline().split())
        parent, left, right = ord(parent) - 65, ord(left) - 65, ord(right) - 65
        if left >= 0:
            tree[parent][1] = left
            tree[left][0] = parent
        if right >= 0:
            tree[parent][2] = right
            tree[right][0] = parent
    if cnt1 == 0:  # 루트에서 시작이므로 루트 찾음
        for i in range(N):
            if tree[i] != [None, None, None] and tree[i][0] == None:
                root = i  # i번 node가 root임
                break
    print(pre(root, tree, [0] * 26))
    print(mid(root, tree, [0] * 26))
    print(post(root, tree, [0] * 26))


def pre(node, tree, added):
    global N, word1, cnt1
    if cnt1 == 0:
        word1 += chr(node + 65)
        added[node] = 1
        cnt1 += 1
    if cnt1 == N:
        return word1
    parent, left, right = tree[node][0], tree[node][1], tree[node][2]
    if left != None:
        if added[left] == 0: #왼쪽에 방문할게 남아있음
            word1 += chr(left + 65)
            added[left] = 1
            cnt1 += 1
            return pre(left, tree, added)
        else:
            if right == None: #왼쪽 방문 끝, 오른쪽은 방문할거 없음. 부모 노드로 돌아감
                return pre(parent, tree, added)
            if right != None:
                if added[right] == 0: #오른쪽은 아직 추가 안됨
                    word1 += chr(right + 65)
                    added[right] = 1
                    cnt1 += 1
                    return pre(right, tree, added)
                else: #오른쪽 노드들도 다 추가 끝남
                    return pre(parent, tree, added)
    else: #왼쪽 node는 없음
        if right == None: # 끝 노드에 도착
            return pre(parent, tree, added)
        else: #오른쪽에 갈 node 있음
            if added[right] == 0:
                word1 += chr(right + 65)
                added[right] = 1
                cnt1 += 1
                return pre(right, tree, added)
            else:
                return pre(parent, tree, added)


def mid(node, tree, added):
    global N, word2, cnt2
    if cnt2 == N:
        return word2
    parent, left, right = tree[node][0], tree[node][1], tree[node][2]
    if left != None:
        if added[left] == 0: #왼쪽노드는 word에 안더해짐
            return mid(left, tree, added)
        else: #왼쪽노드는 word에 이미 더해짐
            if added[node] == 0:
                word2 += chr(node + 65)
                added[node] = 1
                cnt2 += 1
            if right == None:#오른쪽에 방문할 node가 없으면 부모노드로 돌아감
                return mid(parent, tree, added)
            else:
                if added[right] == 0:
                    return mid(right, tree, added)
                else:
                    return mid(parent, tree, added)
    else: #왼쪽에 방문할 node 없음
        if added[node] == 0:
            word2 += chr(node + 65)
            added[node] = 1
            cnt2 += 1
        if right == None:
            if added[node] == 0:
                word2 += chr(node + 65)
                added[node] = 1
                cnt2 += 1
            return mid(parent, tree, added)
        else:
            if added[right] == 0:
                return mid(right, tree, added)
            else:
                return mid(parent, tree, added)


def post(node, tree, added):
    global N, word3, cnt3
    if cnt3 == N:
        return word3
    parent, left, right = tree[node][0], tree[node][1], tree[node][2]
    if left != None:
        if added[left] == 0: #왼쪽에 추가가능한거 있음
            return post(left, tree, added)
        else:
            if right == None: #왼쪽 노드는 word에 추가 완료, 오른쪽 노드는 없음. 현재 node word에 추가하고 parent로 이동
                if added[node] == 0:
                    word3 += chr(node + 65)
                    added[node] = 1
                    cnt3 += 1
                return post(parent, tree, added)
            else:
                if added[right] == 1:
                    if added[node] == 0:
                        word3 += chr(node + 65)
                        added[node] = 1
                        cnt3 += 1
                    return post(parent, tree, added)
                else:
                    return post(right, tree, added)
    else:
        if right == None:
            if added[node] == 0:
                word3 += chr(node + 65)
                added[node] = 1
                cnt3 += 1
            return post(parent, tree, added)
        else:
            if added[right] == 1:
                if added[node] == 0:
                    word3 += chr(node + 65)
                    added[node] = 1
                    cnt3 += 1
                return post(parent, tree, added)
            else:
                return post(right, tree, added)


if __name__ == '__main__':
    main()

import sys


def main():
    global N
    N = int(sys.stdin.readline())
    tree = [[None, None, None] for i in range(26)] #부모, left, right 배치
    for i in range(N):
        parent, left, right = map(str, sys.stdin.readline().split())
        parent, left, right = ord(parent) - 65, ord(left) - 65, ord(right) - 65
        if 0 <= left:
            tree[parent][1] = left
            tree[left][0] = parent
        if 0 <= right:
            tree[parent][2] = right
            tree[right][0] = parent
    root = findroot(tree, N)
    pre(tree, root, [''] * N, root, [0], [0] * 26)
    #mid(tree, root, [''] * N, root, [0], [0] * 26)
    #post(tree, root, [''] * N, root, [0], [0] * 26)


def findroot(tree, N):
    for i in range(N):
        if tree[i] != [None, None, None] and tree[i][0] == None:
            return i


def pre(tree, root, word, node, cnt, visit): # node: 현재 node
    global N
    if cnt[0] == 0: #첫시작
        visit[root] = 1
        word[cnt[0]] = chr(root + 65)
        cnt = [1]
    if cnt[0] == N: #순회 완료
        for i in range(N):
            print(word[i], end='')
        return
    left, right = tree[node][1], tree[node][2]
    if left != None and visit[left] == 0: #왼쪽으로 갈수있고 이미 방문한 node가 아니면
        visit[left] = 1
        word[cnt[0]] = chr(left + 65)
        cnt[0] += 1
        pre(tree, root, word, left, cnt, visit)
    if right != None and visit[right] == 0:
        visit[right] = 1
        word[cnt[0]] = chr(right + 65)
        cnt[0] += 1
        pre(tree, root, word, right, cnt, visit)
    if left == None and right == None: # 밑에 아무것도 없으니 부모node로 돌아간다
        node = tree[node][0]
        pre(tree, root, word, node, cnt, visit)


def mid(tree, root, word, node, cnt, visit):
    global N
    if cnt == [0]: #시작할때
        node = root #맨 왼쪽 점을 node로 시작
        while tree[node][1] != None:
            node = tree[node][1] # 계속 왼쪽밑으로감
        word[cnt[0]] = chr(node + 65)
        visit[node] = 1
        cnt[0] += 1
    if cnt[0] == N:
        for i in range(N):
            print(word[i], end='')
        return
    parent, left, right = tree[node][0], tree[node][1], tree[node][2]
    if left == None and right == None: #밑에 아무것도 없어서 word에 추가함
        word[cnt[0]] = chr(node + 65)
        cnt[0] += 1
        visit[node] = 1
        mid(tree, root, word, parent, cnt)
    if left != None and visit[left] == 1 and visit[node] == 0: #왼쪽에 있는건 다 방문해서 word에 추가함 
        word[cnt[0]] = chr(left + 65)
        cnt[0] += 1
        visit[node] = 1
        if right != None and visit[right] == 0: #오른쪽으로 가는것 가능
            mid(tree, root, word, node, cnt, visit)
        if parent != None:
            mid(tree, root, word, node, cnt, visit)
    if right != None and visit[right] == 1 and visit[node] == 0:
        word[cnt[0]] = chr(left + 65)
        cnt[0] += 1
        visit[node] = 1
            
        
        








def post(tree, root, word, node, cnt, visit):
    global N
    return 0


if __name__ == '__main__':
    main()

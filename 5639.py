import sys
sys.setrecursionlimit(pow(10, 6))


def main():
    nodes = []
    while 1:
        try:
            nodes.append(int(sys.stdin.readline()))
        except:
            break
    maketree(nodes[0], nodes[1:])


def maketree(root, childrens):
    if len(childrens) == 0:
        print(root)
        return
    sliceIdx = None # root 보다 큰 값 중 제일 작은 node를 가리키는 idx를 찾음
    start, end = 0, len(childrens) - 1
    while start <= end:
        mid = (start + end) // 2
        if childrens[mid] < root:
            start = mid + 1
        else:
            sliceIdx = mid
            end = mid - 1
    if sliceIdx == None:
        maketree(childrens[0], childrens[1:]) # left만 있음
    elif sliceIdx == 0:
        maketree(childrens[0], childrens[1:])  # right만 있음
    else:
        maketree(childrens[0], childrens[1:sliceIdx])
        maketree(childrens[sliceIdx], childrens[sliceIdx + 1:])
    print(root)
    

if __name__ == '__main__':
    main()

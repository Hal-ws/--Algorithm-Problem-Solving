import sys
import heapq
from collections import deque



def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N, M = map(int, sys.stdin.readline().split())
        dList = list(map(int, sys.stdin.readline().split()))  # 문서 리스트
        print(getans(N, M, dList))


def getans(N, M, dList):
    q = deque()
    ans = 1  # 출력되는 순서
    iHeap = []  # 우선순위 담은 Heap
    for i in range(N):
        q.append([dList[i], i])  # 중요도, 문서 idx 저장
        heapq.heappush(iHeap, -dList[i])
    while 1:
        curImportant = q[0][0]  # 현재 문서의 중요도
        if curImportant == -iHeap[0]:  # 출력 가능한지 확인(뒤에 중요도가 더 높은 문서가 있는지 확인)
            if q[0][1] == M:  # 현재 index가 M이라면 종료
                return ans
            q.popleft()  # 출력했으니 q에서 제거
            heapq.heappop(iHeap)
            ans += 1  #
        else:  # 출력 불가능. 맨 뒤로 보냄
            tmp = q.popleft()
            q.append(tmp)


if __name__ == "__main__":
    main()

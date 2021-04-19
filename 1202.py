import sys
import heapq


def main():
    N, K = map(int, sys.stdin.readline().split())
    jewerly = []
    possible_jewerly = []
    bags = []
    answer = 0
    for i in range(N):
        M, V = map(int, sys.stdin.readline().split())
        heapq.heappush(jewerly, [M, V]) # 무게, 가치
    for i in range(K):
        bags.append(int(sys.stdin.readline()))
    bags.sort()
    for maxM in bags:
        while len(jewerly) > 0:
            tmp = heapq.heappop(jewerly)
            M, V = tmp[0], tmp[1]
            if M <= maxM:
                heapq.heappush(possible_jewerly, -V)
            else:
                heapq.heappush(jewerly, [M, V])
                break
        if len(possible_jewerly) > 0:
            answer += (-1 * heapq.heappop(possible_jewerly))
    print(answer)


if __name__ == '__main__':
    main()

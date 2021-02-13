import sys
import heapq


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        k = int(sys.stdin.readline())
        dic = {}
        minQ = []
        maxQ = []
        for i in range(k):
            a, b = map(str, sys.stdin.readline().split())
            b = int(b)
            if a == 'I':
                if dic.get(b) == None: #아직 없을때
                    dic[b] = 1
                    heapq.heappush(minQ, b)
                    heapq.heappush(maxQ, -b)
                else:
                    dic[b] += 1
                    heapq.heappush(minQ, b)
                    heapq.heappush(maxQ, -b)
            else:
                if b == 1: #최댓값 삭제
                    while 1:
                        if len(maxQ) == 0:
                            break
                        key = -1 * heapq.heappop(maxQ)
                        if dic[key] > 0: #아직 남아 있을때
                            dic[key] -= 1
                            break
                else: #최솟값 삭제
                    while 1:
                        if len(minQ) == 0:
                            break
                        key = heapq.heappop(minQ)
                        if dic[key] > 0: #아직 남아 있을때
                            dic[key] -= 1
                            break
        maxV, minV = None, None        
        while 1:
            if len(maxQ) == 0:
                break
            key = -1 * heapq.heappop(maxQ)
            if dic[key] > 0:
                maxV = key
                break
        while 1:
            if len(minQ) == 0:
                break
            key = heapq.heappop(minQ)
            if dic[key] > 0:
                minV = key
                break
        if maxV == minV == None:
            print('EMPTY')
        else:
            print('%s %s' %(maxV, minV))


if __name__ == '__main__':
    main()

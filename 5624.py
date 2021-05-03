import sys


def main():
    N = int(sys.stdin.readline())
    nList = list(map(int, sys.stdin.readline().split()))
    numSet = {} # 1개만 있는것
    combined = {} # 2개를 섞은것
    numSet[nList[0]] = 1
    combined[nList[0] + nList[0]] = 1
    answer = 0
    for i in range(1, N):
        val = nList[i]
        combined[val] = 1
        flag = 0
        for j in range(i):
            if combined.get(val - nList[j]) != None:
                flag = 1
        for j in range(i + 1):
            combined[val + nList[j]] = 1
        if flag:
            answer += 1
    print(answer)


if __name__ == '__main__':
    main()

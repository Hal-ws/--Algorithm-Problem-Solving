N = int(input())

def move(start, end):
    distance = end - start
    if distance == 0:
        print('check')
        return 0
    else:
        i = 1
        while 1:
            if i * i >= distance:
                break
            i += 1
        if distance == i * i or distance > (i * i + (i - 1) * (i - 1)) // 2:
            return 2*i - 1
        else:
            return 2*i - 2


for i in range(N):
    x, y = map(int, input().split())
    print(move(x, y))

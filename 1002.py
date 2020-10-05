import math
T  = int(input())

def checkCross(smallR, largeR, distance):
    if(smallR + largeR > distance and largeR - smallR < distance):
        print(2)
    elif((smallR + largeR)*(smallR + largeR) == distance*distance or (largeR - smallR)*(largeR - smallR) == distance*distance):
        print(1)
    else:
        print(0)

i = 0
while(i < T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = math.sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1))
    if(r1 > r2):
        checkCross(r2, r1, d)
    elif(r1 < r2):
        checkCross(r1, r2, d)
    else:
        if(x1 == x2 and y1 == y2):
            print(-1)
        elif(r1 + r2 < d):
            print(0)
        elif((r1 + r2)*(r1 + r2) == d*d):
            print(1)
        else:
            print(2)
    i += 1

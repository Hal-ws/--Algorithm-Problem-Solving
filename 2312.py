M = int(input())

case = 0

def devidingN(N, a, b):
    while(N % a == 0): ## 안나눠질때까지 나눈다
        N = N // a
        b = b + 1
    print(str(a) + ' ' + str(b))
    return N

while(case < M):
    N = int(input())
    list = [2, 0]
    while(N > 1):
        if(N % list[0] == 0):
            N = devidingN(N, list[0], list[1])
        list[0] += 1
    case += 1

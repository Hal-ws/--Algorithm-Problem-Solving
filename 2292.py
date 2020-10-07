N = int(input())

def getGroup(n):
    if(n <= 2):
        return n
    else:
        return 3*n*n - 9*n + 8
i = 1
while(True):
    if(getGroup(i) <= N and N < getGroup(i + 1)):
        print(i)
        break
    else:
        i += 1

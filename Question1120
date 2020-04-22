A, B = map(str, input().split())

def getsame(strA, strB):
    cnt = 0
    for i in range(len(strA)):
        if strA[i] == strB[i]:
            cnt += 1
    return cnt

t = []
for i in range(len(B) - len(A) + 1):
    t.append(getsame(A, B[i:i + len(A)]))
print(len(A) - max(t))

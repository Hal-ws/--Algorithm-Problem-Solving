N, K, I = map(int, input().split())

def checkmatch(K, I):
    if (min(K, I) % 2 == 1) and max(K, I) - min(K, I) == 1:
        return True
    return False
def nextround(N):
    if N % 2 == 1:
        return N // 2 + 1
    return N // 2

round = 1
for i in range(17):
    if checkmatch(K, I):
        break
    K = nextround(K)
    I = nextround(I)
    round += 1

if round == 18:
    print(-1)
else:
    print(round)

N, K = map(int, input().split(' '))
Ai = 0
coinList = []
answer = 0 ## coin의 갯수

while(Ai < N):
    coinList.append(int(input()))
    Ai += 1
start = len(coinList) - 1
while(K > 0): ## 돈이 0이 될때까지 계속 감소하는걸로 한다
    if(K < coinList[start]):
        start -= 1
    else:
        answer = answer + K  // coinList[start] ## 몫 만큼 counting 하는 동전에 추가
        K = K % coinList[start] ## k값은 나머지로 변경
        start -= 1

print(answer)

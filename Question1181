import sys
N = int(input())

words = []
lenAndSeq = []
for i in range(N):
    temp = sys.stdin.readline()
    words.append(temp) ## 들어온 순서대로 정렬
    lenAndSeq.append([len(temp), i])

lenAndSeq = sorted(lenAndSeq)
cnt = 0
std = 0 ## 길이의 기준점이 되는 Idx
while(cnt < N):
    temp = []  ## 길이 짧은 word를 저장할 array
    temp.append(words[lenAndSeq[std][1]]) ## 일단 처음으로 temp에 word를 저장해야함
    cnt += 1
    i = std + 1
    while(i < len(lenAndSeq)):
        if(lenAndSeq[i][0] == lenAndSeq[std][0]): ## 기준이 되는 단어의 길이와 같을때
            temp.append(words[lenAndSeq[i][1]])
            cnt += 1
            i += 1
        else: ## 기준이 되는 단어와 길이가 다를때
            std = i
            break
    temp = sorted(temp)
    i = 1
    while(i < len(temp)):
        if(temp[i] == temp[i - 1]):
            del temp[i]
            i -= 1
        i += 1
    for i in range(len(temp)):  ## 짧은 array 부터 출력
        print(temp[i][0:-1])

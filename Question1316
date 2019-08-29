N = int(input())

i = 0
cnt = N
while(i < N):
    inputWord = input()
    startIdx = 0
    endIdx = len(inputWord) - 1
    while(startIdx < len(inputWord) - 1):
        startAl = inputWord[startIdx]
        while(endIdx > startIdx):
            if(inputWord[endIdx] == inputWord[startIdx]):
                break
            endIdx -= 1
        if(endIdx - startIdx > 1):
            j = startIdx + 1
            while(j < endIdx):
                if(inputWord[j] != inputWord[startIdx]):
                    cnt -= 1
                    break
                else:
                    j += 1
        startIdx = endIdx + 1
        endIdx = len(inputWord) - 1
    i += 1
print(cnt)

S = input()
wordList = []
lS = len(S)
for i in range(lS):
    wordList.append(S[i:lS])
wordList.sort()
for i in range(lS):
    print(wordList[i])

L, P = map(int, input().split())

numInNews = list(map(int, input().split()))
trueNum = L * P

for i in range(len(numInNews)):
	print(numInNews[i] - trueNum, end=' ')

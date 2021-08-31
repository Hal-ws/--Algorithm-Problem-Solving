N, M = map(int, input().split())
myCard = list(map(int, input().split()))
myCard.sort(reverse=True)
cardList = [0] * (N * M + 1)  # 사용한 카드 확인을 위해 list선언
for card in myCard:
    cardList[card] = 1  # 내 카드는 중복
for j in range(len(cardList) - 1, 0, -1):
    if cardList[j] == 0:
        strongCard = j
        break
for j in range(1, len(cardList)):
    if cardList[j] == 0:
        weekCard = j
        break
answer = 0
for thisCard in myCard:
    cardList[strongCard] = 1  # 제일 강한 카드 한장을 사용함
    if strongCard < thisCard:
        answer += 1
    for j in range(strongCard - 1, 0, -1):  # 다음 strong card를 골라야함
        if cardList[j] == 0:
            strongCard = j
            break
    cnt = 0
    while cnt < N - 2:  # 작은 순서대로 카드를 N - 2장 사용
        if cardList[weekCard] == 0:  # 사용 안했음
            cardList[weekCard] = 1
            cnt += 1
        weekCard += 1
print(answer)

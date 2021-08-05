def main():
    S = input()
    numStack = [] # 슛자 group과 그 숫자가 시작한 idx를 저장
    pStack = [] # 괄호와 해당 괄호의 idx를 저장
    cnt = 0
    idx = None
    for i in range(len(S)):
        flag = 1
        if S[i] != '(' and S[i] !=')':
            if idx == None:
                idx = i
            cnt += 1
        else:
            if S[i] == '(':
                numStack.append([cnt, int(S[i - 1]), idx])
                pStack.append(['(', i])
                idx = None
            if S[i] == ')':
                if S[i - 1] != ')' and S[i - 1] != '(': # 닫는 괄호 바로앞에 숫자가 있는경우
                    val = int(S[i - 1])
                    numStack.append([cnt, val, idx])
                if S[i - 1] == '(' or pStack[-1][1] > numStack[-1][2]:
                    pStack.pop()
                    flag = 0
                if flag:
                    pIdx = pStack[-1][1]
                    pStack.pop()
                    tmp = numStack.pop()
                    culCnt, val, nIdx = tmp[0], tmp[1], tmp[2]
                    while len(numStack) > 0: # 해당 괄호 안에 있는 값들을 전부 처리함
                        tmp = numStack.pop()
                        if tmp[2] < pIdx: # 괄호 밖의 값임
                            numStack.append(tmp)
                            break
                        culCnt += tmp[0]
                        nIdx = tmp[2]
                    numStack.append([culCnt, val, nIdx])
                    tmp1 = numStack.pop()
                    tmp2 = numStack.pop()
                    if tmp2[1] == 0:
                        val = int(S[tmp2[2]])
                    else:
                        val = tmp1[1]
                    numStack.append([tmp1[0] * tmp2[1] + tmp2[0] - 1, val, tmp2[2]])
                    if numStack[-1][0] == 0:
                        numStack.pop()
                else: # ()를 처리
                    tmp = numStack.pop()
                    numStack.append([tmp[0] - 1, int(S[tmp[2]]), tmp[2]])
                idx = None
            cnt = 0
    answer = cnt
    while len(numStack) > 0:
        tmp = numStack.pop()
        answer += tmp[0]
    print(answer)


if __name__ == '__main__':
    main()

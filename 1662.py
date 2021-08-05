def main():
    S = input()
    numStack = [] # 슛자 group과 그 숫자가 시작한 idx를 저장
    pStack = [] # 괄호와 해당 괄호의 idx를 저장
    cnt = 0
    idx = None
    for i in range(len(S)):
        flag = 1
        print('i: %s' %i)
        if S[i] != '(' and S[i] !=')':
            if idx == None:
                idx = i
            cnt += 1
        else:
            if S[i] == '(':
                numStack.append([cnt, int(S[i - 1]), idx])
                pStack.append(['(', i])
                idx = None
            if S[i] == ')': # 해당 괄호 안에 있는 값들을 전부 처리함
                if S[i - 1] == '(':
                    pStack.pop()
                    flag = 0
                elif S[i - 1] != ')': # 숫자가 있는경우
                    val = int(S[i - 1])
                    numStack.append([cnt, val, idx])
                    print('i: %s' %i)
                    print('numStack: %s' %numStack)
                    pStack.pop()
                else:
                    pIdx = pStack[-1][1]
                    pStack.pop()
                    tmp = numStack.pop()
                    culCnt, val, nIdx = tmp[0], tmp[1], tmp[2]
                    while len(numStack) > 0:
                        tmp = numStack.pop()
                        if tmp[2] < pIdx: # 괄호 밖의 값임
                            numStack.append(tmp)
                            break
                        culCnt += tmp[0]
                        nIdx = tmp[2]
                    numStack.append([culCnt, val, nIdx])
                if flag:
                    tmp1 = numStack.pop()
                    tmp2 = numStack.pop()
                if tmp2[1] == 0:
                    val = int(S[tmp2[2]])
                else:
                    val = tmp1[1]
                numStack.append([tmp1[0] * tmp2[1] + tmp2[0] - 1, val, tmp2[2]])
                if numStack[-1][0] == 0:
                    numStack.pop()
                idx = None
            cnt = 0
        print(numStack)
    answer = cnt
    while len(numStack) > 0:
        tmp = numStack.pop()
        answer += tmp[0]
    print(answer)


if __name__ == '__main__':
    main()

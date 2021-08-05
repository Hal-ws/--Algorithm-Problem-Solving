def main():
    S = input()
    numStack = [] # 슛자 group과 그 숫자가 시작한 idx를 저장
    pStack = [] # 괄호와 해당 괄호의 idx를 저장
    cnt = 0
    idx = None
    for i in range(len(S)):
        if S[i] != '(' and S[i] !=')':
            if idx != None:
                idx = i
            cnt += 1
        else:
            if S[i] == '(':
                numStack.append([cnt - 1, int(S[i - 1]), idx])
                pStack.append(['(', i])
                idx = None
            if S[i] == ')':
                if S[i - 1] != ')': # 숫자가 있을때
                    num, tIdx = int(S[i - 1]), idx
                    numStack.append([cnt, int(S[i - 1]), idx])
                while 1:
                    pIdx = pStack[-1][1]
                idx = None
            cnt = 0


if __name__ == '__main__':
    main()

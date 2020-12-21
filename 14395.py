from collections import deque


def main():
    s, t = map(int, input().split())
    if s == t:
        print(0)
        return
    q = deque()
    q.append(['*', s * s, 1])
    q.append(['+', s + s, 1])
    case = [None, None]
    visit = set()
    visit.add(s * s)
    visit.add(s + s)
    visit.add(s)
    while len(q) > 0:
        sign = q[0][0]
        curN = q[0][1]
        length = q[0][2]
        if curN == t:
            case[0] = sign
            break
        if sign == '+' * length and t < curN:
            break
        if curN * curN not in visit and curN * curN <= t:
            q.append([sign + '*', curN * curN, length + 1])
            visit.add(curN * curN)
        if curN + curN not in visit and curN + curN <= t:
            q.append([sign + '+', curN + curN, length + 1])
            visit.add(curN + curN)
        q.popleft()
    q = deque()
    q.append(['/', 1, 1])
    visit = set()
    visit.add(s)
    visit.add(1)
    while len(q) > 0:
        sign = q[0][0]
        curN = q[0][1]
        length = q[0][2]
        if curN == t:
            case[1] = sign
            break
        if sign == '/' + '+' * (length - 1) and t < curN:
            break
        if curN * curN not in visit and curN * curN <= t:
            q.append([sign + '*', curN * curN, length + 1])
            visit.add(curN * curN)
        if curN + curN not in visit and curN + curN <= t:
            q.append([sign + '+', curN + curN, length + 1])
            visit.add(curN + curN)
        q.popleft()
    if case[0] == case[1]:
        print(-1)
    elif case[0] == None and case[1] != None:
        print(case[1])
    elif case[0] != None and case[1] == None:
        print(case[0])
    else:
        if len(case[0]) < len(case[1]):
            print(case[0])
        elif len(case[0]) > len(case[1]):
            print(case[1])
        else:
            print(case[0])


if __name__ == '__main__':
    main()

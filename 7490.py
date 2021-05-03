import sys
from itertools import product


def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        nList = [str(i) for i in range(1, N + 1)]
        signCases = list(product(['+', '-', ' '], repeat=N - 1))
        ansList = []
        for case in signCases:
            result = ''
            for i in range(N - 1):
                result += nList[i]
                result += case[i]
            result += nList[-1]
            cal = []
            tmp = ''
            for i in range(len(result)):
                if result[i] == '+' or result[i] == '-':
                    cal.append(int(tmp))
                    cal.append(result[i])
                    tmp = ''
                elif result[i] == ' ':
                    tmp += ''
                else:
                    tmp += result[i]
            cal.append(int(tmp))
            calResult = cal[0]
            for i in range(1, len(cal) - 1, 2):
                if cal[i] == '-':
                    calResult -= cal[i + 1]
                if cal[i] == '+':
                    calResult += cal[i + 1]
            if calResult == 0:
                ansList.append(result)
        ansList.sort()
        for tmp in ansList:
            print(tmp)
        print()


if __name__ == '__main__':
    main()

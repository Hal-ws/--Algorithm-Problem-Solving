import sys


def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        print(chkSignal(sys.stdin.readline()))


def chkSignal(signal):
    l = len(signal) - 1
    signal = signal[:l]
    sIdx = 0
    while sIdx < l:
        if signal[sIdx] == '0':
            if sIdx >= l - 1:
                return 'No'
            if signal[sIdx + 1] == '0':
                return 'No'
            else:
                sIdx += 2
        else: # 1로 시작
            if sIdx >= l - 3:
                return 'No'
            if signal[sIdx + 1] != '0' or signal[sIdx + 2] != '0':
                return 'No'
            flag = 0
            for tIdx in range(sIdx + 1, l):
                if signal[tIdx] == '1':
                    flag = 1
                    if tIdx == l - 1:
                        return 'Yes'
                    break
            if flag == 0:
                return 'No'
            flag = 0
            for idx2 in range(tIdx + 1, l):
                if signal[idx2] != '1':
                    if idx2 == l - 1:
                        return 'No'
                    if idx2 == l - 2:
                        sIdx = idx2
                        flag = 1
                        break
                    else: # idx2 < l - 2:
                        if signal[idx2 + 1] == '1': # 다음에 오는게 01임
                            sIdx = idx2
                            flag = 1
                            break
                        else: # 다음에 오는게 100이 옴
                            sIdx = idx2 - 1
                            flag = 1
                            break
            if flag == 0:
                return 'Yes'
            if sIdx <= tIdx:
                return 'No'
    return 'YES'


if __name__ == '__main__':
    main()

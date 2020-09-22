import sys
from queue import PriorityQueue


def main():
    plusque, minusque, cntPlus, cntMinus = PriorityQueue(), PriorityQueue(), 0, 0
    N = int(sys.stdin.readline())
    for i in range(N):
        query = int(sys.stdin.readline())
        if query == 0:
            if cntPlus > 0 and cntMinus > 0:
                plusVal, minusVal = plusque.get(), minusque.get()
                if minusVal <= plusVal:
                    print(minusVal * (-1))
                    cntMinus -= 1
                    plusque.put(plusVal)
                else:
                    print(plusVal)
                    cntPlus -= 1
                    minusque.put(minusVal)
            elif cntPlus > 0 and cntMinus == 0:
                print(plusque.get())
                cntPlus -= 1
            elif cntPlus == 0 and cntMinus > 0:
                print(minusque.get() * (-1))
                cntMinus -= 1
            else:
                print(0)
        else:
            if query < 0:
                minusque.put(query * (-1))
                cntMinus += 1
            else:
                plusque.put(query)
                cntPlus += 1


if __name__ == "__main__":
    main()

import sys


def main():
    forest = {}
    total = 0
    woodList = []
    while 1:
        wood = sys.stdin.readline().rstrip()
        if wood == '':
            break
        if forest.get(wood) == None:
            forest[wood] = 1
            woodList.append(wood)
        else:
            forest[wood] += 1
        total += 1
    woodList.sort()
    for wood in woodList:
        print('%s %.4f' %(wood, 100 * forest[wood] / total))


if __name__ == '__main__':
    main()

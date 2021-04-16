import sys


def main():
    N, M = map(int, sys.stdin.readline().split())
    books = []
    memory = int('0b11111111111111111111111111', 2)
    for i in range(N):
        tmp = sys.stdin.readline()
        word = 0
        for j in range(len(tmp) - 1):
            word = word | pow(2, ord(tmp[j]) - 97)
        books.append(word)
    for i in range(M):
        a, b = map(str, sys.stdin.readline().split())
        cnt = 0
        if a == '1':
            memory = memory - pow(2, ord(b) - 97)
        else:
            memory = memory | pow(2, ord(b) - 97)
        for word in books:
            if memory == (memory | word):
                cnt += 1
        print(cnt)


if __name__ == '__main__':
    main()

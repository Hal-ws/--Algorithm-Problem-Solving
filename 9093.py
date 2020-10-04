import sys


def main():
    T = int(sys.stdin.readline())
    for i in range(T):
        sentence = list(map(str, sys.stdin.readline().split()))
        ls = len(sentence)
        for j in range(ls):
            sentence[j] = reverse(sentence[j])
        for j in range(ls):
            print(sentence[j], end= ' ')


def reverse(word):
    lw = len(word)
    reversed = ''
    for i in range(lw - 1, -1, -1):
        reversed += word[i]
    return reversed


if __name__ == "__main__":
    main()

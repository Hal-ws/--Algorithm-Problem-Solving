def main():
    r1, c1, r2, c2 = map(int, input().split())
    M = max(abs(r1), abs(r2), abs(c1), abs(c2))
    paper = [[0 for i in range(2 * M + 1)] for j in range(2 * M + 1)]
    n = 1
    for i in range(M + 1):
        paper[M + i][M + i] = pow((2 * i + 1), 2)
        paper = cycle(paper, M + i)
    maxlen = len(str(paper[2 * M][2 * M]))
    for i in range(r2 - r1 + 1):
        for j in range(c2 - c1 + 1):
            l = len(str(paper[i][j]))
            print(' ' * (maxlen - l) + str(paper[i][j]), end = ' ')
        print()

def cycle(paper, point):
    val = paper[point][point] - 1
    i, j = point, point
    for k in range((point - 3) * 2):
        j -= 1
        paper[i][j] = val
        val -= 1
    for k in range((point - 3) * 2):
        i -= 1
        paper[i][j] = val
        val -= 1
    for k in range((point - 3) * 2):
        j += 1
        paper[i][j] = val
        val -= 1
    for k in range((point - 3) * 2 - 1):
        i += 1
        paper[i][j] = val
        val -= 1
    return paper

if __name__ == "__main__":
    main()

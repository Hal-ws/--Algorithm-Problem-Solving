def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = merge(A, B, N, M)
    for i in range(N + M):
        print(result[i], end=' ')


def merge(A, B, N, M):
    i, j = 0, 0
    result = []
    while i < N or j < M:
        if i == N or j == M:
            if i == N:
                result.append(B[j])
                j += 1
                if j == M :
                    break
            if j == M:
                result.append(A[i])
                i += 1
                if i == N:
                    break
        else:
            if A[i] < B[j]:
                result.append(A[i])
                i += 1
            elif A[i] > B[j]:
                result.append(B[j])
                j += 1
            else:
                result.append(A[i])
                result.append(B[j])
                i += 1
                j += 1
    return result


if __name__ == "__main__":
    main()

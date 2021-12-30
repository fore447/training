import itertools

N, M = map(int, input().rstrip().split())
A = [[False] * N for _ in range(N)]
B = [[False] * N for _ in range(N)]

for _ in range(M):
    i, j = map(int, input().rstrip().split())
    i -= 1
    j -= 1
    A[i][j] = A[j][i] = True

for _ in range(M):
    i, j = map(int, input().rstrip().split())
    i -= 1
    j -= 1
    B[i][j] = B[j][i] = True

ans = False
for p in itertools.permutations(range(N)):
    ok = True
    for i in range(N):
        for j in range(N):
            if A[i][j] != B[p[i]][p[j]]:
                ok = False
    if ok:
        ans = True
print("Yes" if ans else "No")
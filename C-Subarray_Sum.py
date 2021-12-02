N, K, S = map(int, input().rstrip().split())

A = [S]*N

for i in range(K, N):
    if A[i] < 10**9:
        A[i] = S+1
    else:
        A[i] = 1
print(*A)
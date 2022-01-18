import bisect
N, Q = map(int, input().rstrip().split())
A = sorted(list(map(int, input().rstrip().split())))

Ans = []
for i in range(Q):
    x = int(input())
    Ans.append(N - bisect.bisect_left(A, x))

for i in Ans:
    print(i)
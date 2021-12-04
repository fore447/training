N, K, X, Y = [int(input().rstrip()) for i in range(4)]
if K <= N:
    print(X*K + Y*(N-K))
else:
    print(X*N)

# N,K,X,Y=[int(input()) for i in range(4)]
# print(N*X-(X-Y)*max(N-K,0))
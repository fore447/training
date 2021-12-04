N, Q = map(int, input().rstrip().split())
A = [0]*N
for i in range(Q):
    L, R, T = map(int, input().strip().split())
    for j in range(L-1,R):
        A[j] = T
print(*A, sep='\n')

# N,Q=map(int,input().split())
# a=[0]*N
# for i in range(Q):
#     L,R,T=map(int,input().split())
#     for i in range(L,R+1):
#         a[i-1]=T
# for i in range(N):
#     print(a[i])
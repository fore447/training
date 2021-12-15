N = int(input().rstrip())
A = []
B = []
for i in range(N):
    a,b = map(int, input().rstrip().split())
    A.append(a)
    B.append(b)
ans=2*10**5
for i in range(N):
    for j in range(N):
        if i!=j:
            if A[i] >= B[j] and ans > A[i]:
                ans = A[i]
            elif A[i] < B[j] and ans > B[j]:
                ans = B[j]
        elif ans > A[i]+B[j]:
            ans = A[i]+B[j]

        # if i!=j:
        #     ans=min(ans,max(A[i],B[j]))
        # else:
        #     ans=min(ans,A[i]+B[j])
print(ans)
N, X  = map(int, input().rstrip().split())

A = list(map(int, input().rstrip().split()))

for a in A:
    if a != X:
        print(a, end=' ')

# N,X=map(int,input().split())
# A=list(map(int,input().split()))
# print(*[a for a in A if a!=X])
N, M, C = map(int, input().rstrip().split())
B = list(map(int, input().rstrip().split()))
A =[]
for i in range(N):
    A.append(list(map(int, input().rstrip().split())))
count = 0
for i in range(N):
    sum = C
    for j in range(M):
        sum += A[i][j]*B[j]
    if sum > 0:
        count += 1
print(count)

# N,M,C=map(int,input().split())
# B=list(map(int,input().split()))
# count=0
# for i in range(N):
#     A=list(map(int,input().split()))
#     score=C
#     for j in range(M):
#         score+=A[j]*B[j]
#     if score>0:
#         count+=1
# print(count)
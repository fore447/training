N, M = map(int, input().rstrip().split())
result = [0]*M
rows = [list(map(int, input().rstrip().split())) for i in range(N)]
for row in rows:
    for i in range(1, row[0]+1):
        result[row[i]-1] += 1

count = 0
for i in range(M):
    if result[i] == N:
        count += 1
print(count)

# N,M=map(int,input().split())
# food=set(range(1,M+1))
# for i in range(N):
#     K,*A=map(int,input().split())
#     food&=set(A)
# print(len(food))
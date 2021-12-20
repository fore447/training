N, T = map(int, input().rstrip().split())
min_cost = 1001
for i in range(N):
    c, t = map(int, input().rstrip().split())
    if t <= T and c < min_cost:
        min_cost = c
if min_cost == 1001:
    print('TLE')
else:
    print(min_cost)

# N,T=map(int,input().split())
# min_cost=1001
# for i in range(N):
#     c,t=map(int,input().split())
#     if t<=T:
#         min_cost=min(min_cost,c)
# print("TLE" if min_cost==1001 else min_cost)

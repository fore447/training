N = int(input().rstrip())
S = []
P = []
for i in range(N):
    s, p = input().rstrip().split()
    S.append(s)
    P.append(int(p))
people_num = sum(P)
half_people = people_num//2 + 1
for i in range(N):
    if P[i] >= half_people:
        print(S[i])
        break
    if i == N-1:
        print('atcoder')

# N=int(input())
# S=[]
# P=[]
# for i in range(N):
#     s,p=input().split()
#     S.append(s)
#     P.append(int(p))
# print(S[P.index(max(P))] if max(P)>sum(P)/2 else "atcoder")
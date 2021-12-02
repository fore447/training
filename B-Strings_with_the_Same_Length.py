N = int(input().rstrip())

S, T = input().rstrip().split()

for i in range(N):
    print(S[i]+T[i], end='')

# N=input()
# S,T=input().split()
# print(*[s+t for s,t in zip(S,T)],sep="")
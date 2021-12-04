L, H = map(int, input().rstrip().split())
N = int(input().rstrip())
A = [int(input().rstrip()) for i in range(N)]
for a in A:
    if L <= a <= H:
        print(0)
    elif a < L:
        print(L-a)
    else:
        print(-1)

# L,H=map(int,input().split())
# N=int(input())
# A=[int(input()) for i in range(N)]
# for a in A:
#     print(L-a if L>a else 0 if H>=a else -1)
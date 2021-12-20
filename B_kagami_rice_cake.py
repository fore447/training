N = int(input().rstrip())
d = sorted([int(input()) for i in range(N)])
Ans = len(d)
for i in range(N-1):
    if d[i] == d[i+1]:
        Ans -= 1
print(Ans)

# N=int(input())
# d=[int(input()) for i in range(N)]
# print(len(set(d)))
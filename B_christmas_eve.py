N = int(input().rstrip())
p = [int(input().rstrip()) for i in range(N)]
Ans = 0
max = 0
for row in p:
    Ans += row
    if row > max:
        max = row
print(Ans - max//2)

# N=int(input())
# p=[int(input()) for i in range(N)]
# print(sum(p)-max(p)//2)
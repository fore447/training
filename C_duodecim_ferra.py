L = int(input().rstrip())
# 仕切りと切ったパーツで考える
ans = 1
for i in range(1, 12):
    ans *= L-i
    ans //= i
print(int(ans))

# import math
# N=int(input())
# print(math.factorial(N-1)//(math.factorial(11)*math.factorial(N-12)))
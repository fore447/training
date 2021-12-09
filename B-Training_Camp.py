N = int(input().rstrip())
power = 1
for i in range(1, N+1):
    power *= i
    power %= (10**9+7)
print(power)

# import math
# N = int(input().rstrip())
# power = math.factorial(N)
# print(power % (10**9+7))
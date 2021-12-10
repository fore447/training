import math
P = int(input().rstrip())
max_index = 0
for i in range(1, P):
    if P < math.factorial(i):
        max_index = i-1
        break

coin_count = 0
i = max_index
while P > 0:
    if P >= math.factorial(i):
        P -= math.factorial(i)
        coin_count += 1
    else:
        i += -1
print(coin_count)

# import math
# P=int(input())
# count=0
# for coin in range(10,0,-1):
#     if P>=math.factorial(coin):
#         count+=P//math.factorial(coin)
#         P%=math.factorial(coin)
# print(count)

# import math
# P=int(input())
# count=0
# for coin in range(10,0,-1):
#     while P>=math.factorial(coin):
#         count+=1
#         P-=math.factorial(coin)
# print(count)
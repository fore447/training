N = int(input().rstrip())
for i in range(1, 8):
    if N < 2**i:
        Ans = 2**(i-1)
        break
print(Ans)

# N=int(input())
# div=1
# for i in range(7):
#     if 2**i<=N:
#         div=2**i
# print(div)

# N=int(input())
# div=1
# while div*2<=N:
#     div*=2
# print(div)

# N=int(input())
# print(bin(N))
# print(2**(len(bin(N))-3))

# N=int(input())
# print(2**(N.bit_length()-1))

# import math
# N = int(input().rstrip())
# print(2**int(math.log2(N)))
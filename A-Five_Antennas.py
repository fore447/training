antena = [int(input().rstrip()) for i in range(5)]
k = int(input().rstrip())
if antena[-1] - antena[0] <= k:
    print('Yay!')
else:
    print(':(')

# a, b, c, d, e, k = [int(input()) for i in range(6)]
# print('Yay!' if abs(a-e)<=k else ':(')
# A = int(input().rstrip())
# B = int(input().rstrip())
# C = int(input().rstrip())
# X = int(input().rstrip())
A, B, C, X = [int(input()) for i in range(4)]

# count = 0
# for i in range(A+1):
#     for j in range(B+1):
#         for k in range(C+1):
#             if i*500 + j*100 + k*50 == X:
#                 count += 1           
# print(count)

print([500*a+100*b+50*c for c in range(C+1) for b in range(B+1) for a in range(A+1)].count(X))
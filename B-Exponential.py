X = int(input().rstrip())
max = 1
for b in range(1, X+1):
    for p in range(2, X+1):
        if max < b**p <= X:
            max = b**p
        elif b**p >= max:
            break
print(max)

# X=int(input())
# bp=1
# for b in range(1,X):
#     for p in range(2,X):
#         if b**p<=X:
#             bp=max(bp,b**p)
#         else:
#             break
# print(bp)
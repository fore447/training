N, M, X = map(int, input().rstrip().split())
A = list(map(int, input().rstrip().split()))
right = left = 0
for a in A:
    if X > a:
        right += 1
    else:
        left += 1
if right >= left:
    print(left)
else:
    print(right)

# N,M,X=map(int,input().split())
# A=list(map(int,input().split()))
# left=0
# for a in A:
#     if a>X:
#         break
#     left+=1
# right=M-left
# print(min(left,right))
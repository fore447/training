import bisect
N, Q = map(int, input().rstrip().split())
A = sorted(list(map(int, input().rstrip().split())))

Ans = []
for i in range(Q):
    x = int(input())
    Ans.append(N - bisect.bisect_left(A, x))

for i in Ans:
    print(i)

# N, Q = map(int, input().rstrip().split())
# A = [(i, 10**9) for i in map(int, input().rstrip().split())]

# X = []
# for i in range(Q):
#     x = int(input().rstrip())
#     X.append((x, i))

# AX = sorted(A+X)[::-1]

# ans = [0] * Q
# count = 0
# for a, i in AX:
#     if i < Q:
#         ans[i] = count
#     else:
#         count += 1

# print(*ans, sep='\n')

# N, Q = map(int, input().rstrip().split())
# A = sorted(list(map(int, input().rstrip().split())))

# def binary_search(data, value):
#     ok = len(data)
#     ng = -1
#     while ok - ng > 1:
#         mid = (ok + ng) // 2
#         if data[mid] >= value:
#             ok = mid
#         elif data[mid] < value:
#             ng = mid
#     return ok

# Ans = []
# for i in range(Q):
#     x = int(input().rstrip())
#     Ans.append(N - binary_search(A, x))

# for i in Ans:
#     print(i)
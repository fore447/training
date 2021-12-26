import sys
sys.setrecursionlimit(10**6)

N, X = map(int, input().rstrip().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().rstrip().split()))[1:])

count = 0
def dfs(pos, total):
    global count
    if pos == N:
        if total == X:
            count += 1
        return

    for i in arr[pos]:
        new_total = total * i
        if new_total > X:
            continue
        dfs(pos+1, new_total)

dfs(0, 1)
print(count)